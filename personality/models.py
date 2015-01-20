from django.db import models
from django.conf import settings 
from django.core.validators import MaxValueValidator, MinValueValidator
from timeline.models import Node
from django.db.models import Count,Avg
#from social.models import Friendship

class Reputation(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'myReputations')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendsReputations')
	reputation = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)])

class Review(models.Model):
	node = models.ForeignKey(Node, unique = True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'my_reviews')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendsReviews')
	time = models.DateTimeField(auto_now_add = True)

	def data(self, viewer):

		if self.reviewdraft_set.count == 0:
			return 

		data = {}
		draft = self.reviewdraft_set.order_by('-time')[0]

		data['text'] = draft.text
		data['liked'] = draft.liked
		data['time'] = draft.time
		data['id'] = self.id

		return data

class ReviewDraft(models.Model):
	review = models.ForeignKey(Review)
	text = models.TextField(max_length = 2000)
	liked = models.BooleanField(default = False)
	time = models.DateTimeField(auto_now_add = True)



class Trait(models.Model):
	title  = models.CharField(max_length = 15)
	description  = models.CharField(max_length = 255)

class TraityQuestion(models.Model):
	# trait = models.ForeignKey(Trait)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True)
	text = models.CharField(max_length = 100)
	min_cat = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])


	def stats(self, owner, viewer):
		if owner == viewer:

			data = {}
			data['question'] = self.text
			data['id'] = self.id
			data['rating'] = {}
			data['rating']['total'] = self.feedback_set.filter(user = owner).aggregate(rating = Avg('rating'))['rating']

			return data
		else:
			return None

	def data(self, owner, viewer):
		if owner.is_friend_of(viewer):
			data = {}
			data['question'] = self.text
			data['id'] = self.id

			try:
				feedback = self.feedback_set.get(user = owner, friend = viewer)
				data['rating'] = feedback.rating if feedback.rating != None else 0

			except:
				data['rating'] = 0

			return data
		else:
			return None




class Feedback(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'myFeedbacks')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendsFeedbacks')
	question = models.ForeignKey(TraityQuestion)
	rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])


class FeedbackWrapper(models.Model):
	"""This class encapsultes the privacy and other attributes of feedback related to a user"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	feedback = models.ForeignKey(Feedback)
	seen = models.BooleanField(default = False)
	sent = models.BooleanField(default = False)

	from timeline.models import PostPrivacy
	privacy = models.ForeignKey(PostPrivacy)

		



