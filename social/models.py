from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Count,Avg, Q
# from timeline.models import PostPrivacy


from random import randint


class Location(models.Model):
	address = models.CharField(max_length = 100)
	residents = models.IntegerField(default = 0)

class Place(models.Model):
	name = models.CharField(max_length = 100)
	location = models.ForeignKey(Location, null = True)
	employees = models.IntegerField(default = 0)

class UserManager(BaseUserManager):
	def create_user(self, username, email, firstname, lastname, password = None):
		user = self.model(username = username, email = email, firstname = firstname, lastname = lastname)
		user.set_password(password)
		return user

	def create_superuser(self, username, email, firstname, lastname, password):
		user = self.create_user(username, email, firstname, lastname, password = password)
		user.save()
		return user



import os
def profile_pic_path(instance, filename):
	return os.path.join('profile-pics/%d' % instance.id ,'std', filename)



class User(AbstractBaseUser):

	# Identity	
	firstname = models.CharField(max_length = 15)
	lastname = models.CharField(max_length = 15)
	username = models.CharField(max_length = 15, unique = True)
	email = models.EmailField(unique = True)
	phone_number = models.CharField(null=True, unique = True, max_length = 15)
	dob = models.DateField(null = True)
	home = models.ForeignKey(Location, null = True)
	work = models.ForeignKey(Place, null = True, related_name = "current_workers")
	places = models.ManyToManyField(Place)
	profile_pic = models.ImageField(upload_to = profile_pic_path, null = True)

	def my_friends(self):
		return self.friends.filter(status = 3)

	def name(self):
		return self.firstname + " " + self.lastname

	def url(self):
		return "/#/" + self.username

	def imageUrl(self):
		return self.profile_pic.url if self.profile_pic else None

	def thoughts_rating(self):
		ratings = [(node.rating_set.aggregate(rat = Avg('rating'))['rat']) for node in self.node_set.all()]

		# catering for posts that haven't been rated 
		ratings = [(rating if rating != None else 0) for rating in ratings]
		if len(ratings) > 0:
			return sum(ratings)/ float(len(ratings))
		else:
			return None
		
	# Defualt post privacy
	post_privacy = models.ForeignKey('timeline.PostPrivacy', null = True)

	def __unicode__(self):
		return self.get_full_name()

	# Other helper functions

	def data_for_search(self):
		return {
			"name" : self.name(),
			"url": self.url(),
			"imageUrl": self.imageUrl(),
			"id": self.id,
		}

	def data_for_post(self):
		return {
			"username": self.username,
			"name" : self.name(),
			"url": self.url(),
			"imageUrl": self.imageUrl(),
	}

	def friendship_status(self, person_username):
		result = {}
		try:
			rel = Friendship.objects.get(user = self, friend__username = person_username)
			result['status'] = rel.status % 4
			result['circle'] = rel.circle

		except Friendship.DoesNotExist:
			result['status'] = 0 

		if self.username == person_username:
			result['me'] = True
		else:
			result['me'] = False

		return result



	def is_friend_of(self, person):
		try:
			rel = Friendship.objects.get(user = self, friend = person)
			if rel.status == 3:
				return True
			else:
				return False

		except Friendship.DoesNotExist:
			return False


	# Can this user interact with the given post
	def can_interact_with(self, node):

		if(node.privacy.level > 1 and node.privacy.level != 3):
			if self.is_friend_of(node.owner) or self == node.owner:
				return True
			else:
				return False
		elif node.privacy.level == 3:
			pass

	def can_rate(self,node):
		return self.can_interact_with(node) and node.owner != self


	def next_feedback(self, viewer, exclude = None):

		feedbacks = self.myFeedbacks


		prev_questions_ids = [feedback.question.id for feedback in feedbacks.filter(friend = viewer)]

		from personality.models import TraityQuestion, Feedback


		questions = TraityQuestion.objects.filter(Q(user__id__isnull = True) | Q(user = self))

		if exclude:
			questions = questions.exclude(id__in = exclude)

		questions = questions.exclude(id__in = prev_questions_ids)

		if questions.count() > 0:
			question = questions[0]
		else:
			question = None

		if question: 
			return {"question": question.text, "id": question.id, "rating": 0}
		else:
			questions = TraityQuestion.objects.filter(Q(user__id__isnull = True) | Q(user = self))

			if exclude:
				questions = questions.exclude(id__in = exclude)

			if questions.count() > 0:
				feedback = questions[0].data(self, viewer)
			else:
				questions = TraityQuestion.objects.filter(Q(user__id__isnull = True) | Q(user = self))
				feedback = questions[randint(0, questions.count() - 1)].data(self, viewer)

			return feedback



	def feedbacks(self, viewer):

		from personality.models import TraityQuestion

		questions = TraityQuestion.objects.filter(Q(user__id__isnull = True) | Q(user = self))

		if self == viewer:
			feedbacks = [question.stats(self, viewer) for question in questions]
			toret = []

			for feedback in feedbacks:
				if feedback['rating'] != None:
					toret.append(feedback)

			return toret;
		else:
			return []

	def ranking(self, viewer): 

		data = self.data_for_post()
		data['rating'] = self.myReputations.aggregate(repo = Avg('reputation'))['repo']

		if self == viewer: 
			data['me'] = True
		else:
			data['me'] = False

		return data



	# query helper function
	def nicks(self):
		nicks = []
		for nick_stat in self.friends.values('nick').annotate(count = Count('nick')):
			if nick_stat['nick'] != None:
				nicks.append(nick_stat)

		return nicks



	def reviews(self, viewer, rev_range, prev = None):
		revs = self.my_reviews.order_by('-time')

		if self.is_friend_of(viewer):
			revs = revs.filter(node__privacy__level__in = [2,4])
		elif not self == viewer: 
			revs = revs.filter(node__privacy__level = 4)

		if not prev == None:
			revs = revs.filter(id__lt = prev)


		reviews = [rev.data(viewer) for rev in revs[0:rev_range]]

		return reviews



	
	def repo(self, viewer):
		repo = {}
		repo['total'] = self.myReputations.aggregate(repo = Avg('reputation'))['repo']
		repo['count'] = self.myReputations.count()
		try:
			repo['my'] = self.myReputations.get(friend = viewer).reputation
		except:
			repo['my'] = None

		return repo



	#######################################################################
	# Related to profile 
	#######################################################################

	def profile(self, viewer):
		from social.serializers import UserSerializer
		user_data = UserSerializer(self).data
		user_data['url'] = "/#/" + self.username
		user_data['imageUrl'] = self.imageUrl()
		user_data['name'] = self.firstname + " " + self.lastname
		user_data['places'] = True if self.places.count() >= 3 else False

		user_data['work'] = self.work.name if self.work else None
		user_data['home'] = self.home.address if self.home else None

		# realated to reputation 
		user_data['reputation'] = self.repo(viewer)


		# trim the extra 
		del user_data['dob']
		del user_data['phone_number']
		del user_data['email']

		if self == viewer:
			user_data['me'] = True
		else:
			user_data['me'] = False

		user_data['friendship'] = {}
		if self.is_friend_of(viewer):
			user_data['friendship']['exists'] = True
			user_data['friendship']['circle'] = self.friends.get(friend = viewer).circle
		else: 
			user_data['friendship']['exists'] = False


	# def thougths(self, viewer):
	# 	if viewer.is_friend_of(self):
	# 		thougths = self.posts_set.filter(privacy__level__in = [2,4])



		return user_data

	def get_friendslist(self, list_id):
		try:
			return self.friendslist_set.get(id=list_id) 
		except:
			pass

	# Gives back the list of valid lists fo user from the provided list of list_ids :D
	def get_valid_lists(self, list_ids):

		return [flist for flist in [self.get_friendslist(list_id) for list_id in list_ids] if flist]



	# For the django shit
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['firstname', 'lastname', 'email']

	@property
	def is_superuser(self):
		return self.is_staff

	def has_perm(self, perm, obj=None):
		return self.is_staff

	def has_module_perms(self, app_label):
		return self.is_staff

	def get_short_name(self):
		return self.firstname

	def get_full_name(self):
		return self.firstname + " " + self.lastname


class Friendslist(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length = 50)



class Friendship(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friends')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendOf')
	lists = models.ManyToManyField(Friendslist)
	circle = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)], default = 2)
	nick = models.CharField(max_length=50, null = True)
	status = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)], default = 1)





