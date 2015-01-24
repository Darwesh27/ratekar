from django.db import models
from django.conf import settings 
from django.core.validators import MaxValueValidator, MinValueValidator
from social.models import Friendslist
from django.db.models import Avg, Count
import datetime



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
	time = models.DateTimeField(auto_now_add = True)
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
	# time = models.DateTimeField(null = True, auto_now_add = True)


	# Rating of this node
	def rating(self, viewer):
		rating = self.rating_set.aggregate(total = Avg('rating'))
		rating['count'] = self.rating_set.count()
		try:
			rating['my'] = self.rating_set.get(friend = viewer).rating
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
		post['time'] = self.post.time
		post['thought'] = self.thought()
		post['author'] = self.owner.data_for_post()
		post['rating'] = self.rating(viewer)
		post['mine'] = True if self.owner == viewer else False

		return self.get_data(post)

class Rating(models.Model):
	node = models.ForeignKey(Node)
	friend = models.ForeignKey(settings.AUTH_USER_MODEL)
	rating = models.IntegerField(null = True, validators = [MinValueValidator(1), MaxValueValidator(10)])

	def save(self, *args, **kwargs):
		try:
			n = Notification.objects.get(user = self.node.owner, node = self.node, action = 1)
			n.seen = False
			n.sent = False
			n.save()
		except Notification.DoesNotExist:
			n = Notification(user = self.node.owner, node = self.node, type = self.node.kind, action = 1)
			n.save()

		super(Rating, self).save(*args, **kwargs)


class Comment(models.Model):
	node = models.ForeignKey(Node)
	friend = models.ForeignKey(settings.AUTH_USER_MODEL)
	edited = models.BooleanField(default = False)
	time = models.DateTimeField(auto_now_add = True)

	def save(self, *args, **kwargs):
		try:
			n = Notification.objects.get(user = self.node.owner, node = self.node, action = 2)
			n.seen = False
			n.sent = False
			n.time = datetime.datetime.now()
			n.save()
		except Notification.DoesNotExist:
			n = Notification(user = self.node.owner, node = self.node, type = self.node.kind, action = 2)
			n.time = datetime.datetime.now()
			n.save()

		super(Comment, self).save(*args, **kwargs)


	def condemns(self):
		return self.commentcondemn_set.filter(condemned = True)




	def data(self, viewer):
		draft = self.commentdraft_set.all().order_by('time')[0]
		from timeline.serializers import CommentDraftSerializer
		ser = CommentDraftSerializer(draft).data
		ser['edited'] = self.edited 
		ser['id'] = self.id
		ser['time'] = self.time


		if self.friend == viewer:
			ser['author'] = viewer.data_for_post()

		if self.node.owner == self.friend: 
			ser['author'] = self.friend.data_for_post()

		try:
			condemn = self.commentcondemn_set.get(friend = viewer)
			ser['condemned'] = condemn.condemned
		except:
			ser['condemned'] = False


		ser['condemns'] = self.condemns().count()

		ser['condemners'] = [condemn.friend.name() for condemn in self.condemns()]

		return ser


class CommentCondemn(models.Model):
	comment = models.ForeignKey(Comment)
	friend = models.ForeignKey(settings.AUTH_USER_MODEL)
	condemned = models.BooleanField(default = True)




class CommentDraft(models.Model):
	"""Different edits of a comment"""

	comment = models.ForeignKey(Comment)
	time = models.DateTimeField(auto_now_add = True)
	text = models.TextField()
		

class ThoughtDraft(models.Model):
	"""
	Different edits of a Thought.
	"""

	node = models.ForeignKey(Node)
	time = models.DateTimeField(auto_now_add = True)
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


class Notification(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	node = models.ForeignKey(Node)
	action = models.IntegerField()
	type = models.IntegerField()
	sent = models.BooleanField(default = False)
	seen = models.BooleanField(default = False)
	time = models.DateTimeField(auto_now_add = True)

	def data(self):
		from timeline.serializers import NotificationS
		noti_data = NotificationS(self).data
		noti_data['pid'] = self.node.id

		self.sent = True 
		self.save()

		return noti_data



	


		
		
		
		



