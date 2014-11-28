from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Count,Avg
# from timeline.models import PostPrivacy


# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, username, email, firstname, lastname, password = None):
		user = self.model(username = username, email = email, firstname = firstname, lastname = lastname)
		user.set_password(password)
		return user

	def create_superuser(self, username, email, firstname, lastname, password):
		user = self.create_user(username, email, firstname, lastname, password = password)
		user.save()
		return user


class User(AbstractBaseUser):

	# Identity	
	firstname = models.CharField(max_length = 15)
	lastname = models.CharField(max_length = 15)
	username = models.CharField(max_length = 15, unique = True)
	email = models.EmailField(unique = True)
	phone_number = models.CharField(null=True, unique = True, max_length = 15)
	dob = models.DateField(null = True)

	def name(self):
		return self.firstname + " " + self.lastname

	def url(self):
		return "/#/" + self.username

	def imageUrl(self):
		return "/static/img/mj2.jpg"
		
	# Defualt post privacy
	post_privacy = models.ForeignKey('timeline.PostPrivacy', null = True)

	def __unicode__(self):
		return self.get_full_name()

	# Other helper functions

	def data_for_post(self):
		return {
			"username": self.username,
			"name" : self.name(),
			"url": self.url(),
			"imageUrl": self.imageUrl(),
	}

	def is_friend_of(self, person):
		try:
			rel = Friendship.objects.get(user = self, friend = person)
			if rel.status == 3:
				return True
			else:
				return False

		except Friendship.DoesNotExist:
			return False



	# query helper function
	def nicks(self):
		return self.friends.values('nick').annotate(Count('nick'))
		
	
	def repo(self):
		return self.myRatings.aggregate(repo = Avg('reputation'))


	def profile(self):
		from social.serializers import UserSerializer
		user_data = UserSerializer(self).data
		user_data['reputation'] = self.repo()['repo']
		user_data['url'] = "/#/" + self.username
		user_data['imageUrl'] = "static/img/mj2.jpg"
		user_data['name'] = self.firstname + " " + self.lastname

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





