from personality.models import Reputation, Review, TraityQuestion, Feedback
from social.models import User, Friendslist, Friendship
from social.serializers import UserSerializer, FriendslistSerializer, FriendshipSerializer
from rest_framework.response import Response


def g_info(request, uid , cb, own):
	uid = int(uid)
	try: 
		friend = User.objects.get(pk = uid)
		try:
			if own:
				relation = Friendship.objects.get(user = request.user, friend = friend)
			else:
				relation = Friendship.objects.get(user = friend, friend = request.user)

			if relation.status == 3:
				return cb(friend, relation)
			else:
				return Response({"error": "not friends"})
		except Friendship.DoesNotExist:
			return Response({"error": "not friends"})
	except User.DoesNotExist:
		return Response({"error": "User does not exist"})

def user_info(request, uid, cb):
	return g_info(request, uid, cb, True)

def friend_info(request, uid, cb):
	return g_info(request, uid, cb, False)

def add_to_list(relation, list_id):
	list_id = int(list_id)
	try:
		print "In add to list"
		friends_list = Friendslist.objects.get(pk = list_id)
		if friends_list.user == relation.user:
			print "List is of the user"
			relation.lists.add(friends_list)
			try:
				relation.save()
				return True
		 	except:
				return False
		else:
			print "List is not of the user"
			return False
	except Friendslist.DoesNotExist:
		print "List ni mili"
		return False

def remove_from_list(relation, list_id):
	list_id = int(list_id)
	try:
		friends_list = relation.lists
		if friends_list.user == relation.user:
			relation.lists.remove(friends_list)
			try:
				relation.save()
				return True
		 	except:
				return False
		else:
			return False
	except Friendslist.DoesNotExist:
		return False


