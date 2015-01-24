from rest_framework import serializers
from timeline.models import *

class NodeSerializer(serializers.ModelSerializer):
	"""
	Serializer class for node which only returns id, privacy and kind
	"""
	class Meta:
		model = Node
		fields = ('id', 'kind')
			

class ThoughtDraftSerializer(serializers.ModelSerializer):

	class Meta:
		model = ThoughtDraft
		fields = ('time', 'text')
			
class PostPrivacySerializer(serializers.ModelSerializer):

	class Meta:
		model = PostPrivacy
		fields = ('id', 'level', 'include', 'exclude')
		

class CommentDraftSerializer(serializers.ModelSerializer):

	class Meta:
		model = CommentDraft
		fields = ('time', 'text')


class NotificationS(serializers.ModelSerializer):

	class Meta:
		model = Notification
		fields = ('id', 'action', 'type', 'time')

		

