from rest_framework import serializers
from timeline.models import Node, ThoughtDraft, PostPrivacy

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
		fields = ('created_on', 'text')
			
class PostPrivacySerializer(serializers.ModelSerializer):

	class Meta:
		model = PostPrivacy
		fields = ('id', 'level', 'include', 'exclude')
		

