from rest_framework import serializers
from social.models import User, Friendslist, Friendship

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('firstname', 'lastname', 'username', 'email', 'phone_number', 'dob')


class FriendslistSerializer(serializers.ModelSerializer):

	class Meta:
		model = Friendslist
		fields = ('user', 'title')

class FriendshipSerializer(serializers.ModelSerializer):

	class Meta:
		model = Friendship
		fields = ('user', 'friend', 'lists', 'circle', 'nick', 'status')



