from personality.models import Reputation, Review, TraityQuestion, Feedback
from social.models import User, Friendslist, Friendship
from social.serializers import UserSerializer, FriendslistSerializer, FriendshipSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, add_to_list, friend_info
from api.errors import *


@api_view(['POST'])
def friendship(request):
	if request.method == "POST":
		try: 
			friend_username = request.DATA['user']
			circle = int(request.DATA['circle'])

			user = request.user

			try:
				friend = User.objects.get(username = friend_username)

				if not user.is_friend_of(friend):

					rel1, created = Friendship.objects.get_or_create(user = user, friend = friend)
					rel2, c = Friendship.objects.get_or_create(user = friend, friend = user)

					# if this is a request accept it
					if rel1.status == 1 and rel2.status == 2:
						rel1.status = 3
						rel2.status = 3
					# request already sent from the user, Just change the circle
					elif rel1.status == 2 and rel2.status == 1:
						rel1.circle = circle
					else: 
						rel1.status = 2
						rel2.status = 1

					try: 
						rel1.save()
						rel2.save()

						# request successfully handled 
						return Response({"status": 0, "friendship": request.user.friendship_status(friend_username)})

					except: # Some error occured in the database
						return Response(db_error())
				else: # already friends
					return Response(unauthorized_error())
			except: # this is a fake request
				return Response(no_resource_error())
		except: # no parameter provided
			return Response(query_error())

@api_view(['POST'])
def unfriend(request):

	if request.method == 'POST':
		try:
			friend_username = request.DATA['user']

			try: 
				relation1 = Friendship.objects.get(user = request.user, friend__username = friend_username)
				relation2 = Friendship.objects.get(user__username = friend_username, friend = request.user)

				relation1.status = 4
				relation2.status = 4

				relation1.save()
				relation2.save()

				return Response({"status": 0, "friendship": request.user.friendship_status(friend_username)})
			except: # Atlest one of the user does not exists
				return Response(no_resource_error())
		except: # no parameter provided
			return Response(query_error())


@api_view(['GET'])
def friendship_details(request, username):
	if request.method == 'GET':
		return Response({"friendship": request.user.friendship_status(username)})


@api_view(['GET', 'POST'])
def friendship_circle(request, username):
	if request.method == 'POST':

		try:
			rel = request.user.friends.get(friend__username = username)
		except:
			return Response(no_resource_error())

		circle = request.DATA.get('circle', 2)

		rel.circle = circle
		rel.save()

		return Response({"status": 0, "circle": rel.circle})

	else:
		try:
			rel = request.user.friends.get(friend__username = username)
		except:
			return Response(no_resource_error())

		return Response({"status": 0, "circle": rel.circle})


@api_view(['GET', 'POST'])
def friendship_list(request, uid):
	if request.method == 'POST':
		def cb(friend, relation):
			try:
				list_id = request.DATA["list"]
			except:
				return Response(query_error())
			print "in the callback friend id is %s" %(friend.id)
			added = add_to_list(relation, list_id)
			if added:
				return Response({"message": "Ok"})
			else:
				return Response({"error": "list error"})
			
		return user_info(request, uid, cb)
	elif request.method == "GET":
		return Response({"error": "Abi ni bacha..!!"})


@api_view(['GET', 'POST'])
def friendslist(request):
	if request.method == 'POST':
		try:
			title = request.DATA['title'].lower()
		except:
			return Response(query_error)

		try:
			friendslist = Friendslist.objects.get(user = request.user, title = title)
			return Response({'error': "List Already exists"})
		except Friendslist.DoesNotExist:
			friendslist = Friendslist(user = request.user, title = title)
			friendslist.save()
			return Response({'message': 'ok'})
	elif request.method == 'GET':
		# This code is not doing what it should do 
		lists = request.user.friendslist_set.all()
		return Response(FriendslistSerializer(request.user.get_valid_lists([1,3]), many=True).data)

@api_view(['GET'])
def profile(request, username):
	if request.method == 'GET':

		try:
			person = User.objects.get(username = username)
		except:
			return Response(no_resource_error())

		return Response(person.profile(request.user))


@api_view(['GET', 'POST'])
def friend_requests(request):

	if request.method == "POST":
		exclude = request.DATA.get('exclude', [])

	rels = request.user.friends.filter(status = 1)

	print exclude

	if len(exclude) > 0:
		rels = rels.exclude(friend__username__in = exclude)


	data = {
		"requests": [rel.friend.data_for_post() for rel in rels],
		"status": 0
	}

	return Response(data)

@api_view(['GET'])
def friends(request, username):

	if username == request.user.username:

		user = request.user
		friends = [rel.friend.data_for_post() for rel in user.my_friends()]

		return Response({"status": 0, 'friends': friends})
	else:

		return Response(unauthorized_error())


@api_view(['GET'])
def lists(request, username):

	if username == request.user.username:

		user = request.user
		lists = [rel.friend.data_for_post(user) for rel in user.my_friends()]

		return Response({"status": 0, 'lists': lists})
	else:
		return Response(unauthorized_error())

	
