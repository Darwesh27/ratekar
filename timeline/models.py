from django.db import models
from django.conf import settings 
from django.core.validators import MaxValueValidator, MinValueValidator
from social.models import Friendslist
from django.db.models import Avg, Count



class PostPrivacy(models.Model):
	"""
	Privacy of a post
	"""
	level = models.IntegerField(default = 2, validators = [MinValueValidator(1), MaxValueValidator(5)])
	include = models.ManyToManyField(Friendslist, related_name = "incPosts")
	exclude = models.ManyToManyField(Friendslist, related_name = "excPosts")


class Post(models.Model):
	"""
	That a timeline post wrapper..
	"""
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	kind = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])
	created_on = models.DateTimeField(auto_now_add = True)
	privacy = models.ForeignKey(PostPrivacy)



class Node(models.Model):
	"""
	Kind of a parent class for all the models that can have 
	a rating and that can be commented on
	"""

	post = models.ForeignKey(Post, null = True)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	kind = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])
	privacy = models.ForeignKey(PostPrivacy)


	# Rating of this node
	def rating(self, viewer):
		rating = self.rating_set.aggregate(rating = Avg('rating'))
		rating['count'] = self.rating_set.count()
		try:
			rating['my'] = self.rating_set.get(friend = viewer)
		except:
			rating['my'] = None

		return rating



	# Thought with this node
	def thought(self):
		from timeline.serializers import ThoughtDraftSerializer
		try:
			return ThoughtDraftSerializer(self.thoughtdraft_set.all()[0]).data
		except:
			return None

	def get_data(self, post):

		def get_status(post):
			return post

		def get_photo(post):
			return post

		def get_review(post):
			return post

		def get_share(post):
			return post

		related_func = [get_share, get_photo, get_review, get_share]

		return related_func[post['kind'] - 1](post)

	# returns a complete post
	def get_post(self, viewer):
		from timeline.serializers import NodeSerializer
		post = NodeSerializer(self).data
		post['date'] = self.post.created_on
		post['thought'] = self.thought()
		post['author'] = self.owner.data_for_post()
		post['rating'] = self.rating(viewer)

		return self.get_data(post)

class Rating(models.Model):
	node = models.ForeignKey(Node)
	friend = models.ForeignKey(settings.AUTH_USER_MODEL)
	rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)])




class ThoughtDraft(models.Model):
	"""
	Different edits of a Thought.
	"""

	node = models.ForeignKey(Node)
	created_on = models.DateField(auto_now_add = True)
	text = models.TextField()



class Status(models.Model):
	"""
	A post type.. With just a thought..
	"""

	node = models.ForeignKey(Node, primary_key = True)


class Share(models.Model):
	"""
	Model for a typical share which stores which post is being shared
	"""

	node = models.ForeignKey(Node, primary_key = True)
	post = models.ForeignKey(Post)

		

# class Photo(django.models):
# 	"""
# 	Encapsulating a single photo
# 	"""
# 	# check for photo modeling 
# 	node = models.ForeignKey(Node)
#	status = models.ForeignKey(Status, null = True)


# class PhotoDescription(models.Model):
# 	"""
# 	Different edits of the photo description the newest will be shown
# 	"""

# 	photo = models.ForeignKey(Photo)
# 	description = models.CharField()
# 	created_on = models.DateField(auto_now_add = True)


		
		
		
		



