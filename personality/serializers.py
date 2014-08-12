from rest_framework import serializers
from personality.models import Reputation, Review, Trait, TraityQuestion, Feedback

class ReputationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Reputation 
		fields = ('relation', 'reputation')


class ReviewSerializer(serializers.ModelSerializer):

	class Meta:
		model = Review 
		fields = ('relation', 'review', 'liked')

class TraityQuestionSerializer(serializers.ModelSerializer):

	class Meta:
		model = TraityQuestion
		fields = ('text', 'min_cat')


class FeedbackSerializer(serializers.ModelSerializer):

	class Meta:
		model = Feedback
		fields = ('relation', 'question', 'rating')


