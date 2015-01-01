from personality.models import Reputation, Review, TraityQuestion, Feedback
from social.models import User, Friendslist, Friendship
from social.serializers import UserSerializer, FriendslistSerializer, FriendshipSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, add_to_list, friend_info
from api.errors import db_error, query_error, wrong_credentials_error, no_resource_error


@api_view(['POST', 'GET'])
def friendship(request):
	
	if request.method == "POST":

		try:
			friend_username = request.DATA['user']
			circle = int(request.DATA['circle'])
		except:
			return Response(query_error())

		user = request.user

		try:
			friend = User.objects.get(username = friend_username)
		except:
			return Response(no_resource_error())


		relation1, created = Friendship.objects.get_or_create(user = user, friend = friend)

		# A new request is being generated  
		if created: 
			relation2 = Friendship(user = friend , friend = user, status = 1)

			relation1.circle = circle

			relation1.save()
			relation2.save()

		else:

			relation2 = Friendship.objects.get(user__username = friend_username, friend = user)

			# Accept the request 
			if relation1.status == 1 and relation2.status == 2:
				relation1.status = 3
				relation2.status = 3

				relation1.circle = circle

				relation1.save()
				relation2.save()

			# Only change the circle in request
			elif relation1.status == 2 and relation2.status == 1:

				relation1.circle = circle

				relation1.save()
				relation2.save()

			# Revoke an old Friendship, Send request..
			elif relation1.status != 3 and relation2.status != 3:

				relation1.status = 2
				relation2.status = 1

				relation1.circle = circle

				relation1.save()
				relation2.save()
			else:

				return Response(no_resource_error())


		return Response({"status": 0, "friendship": request.user.friendship_status(friend_username)})

	elif request.method == 'GET':
		if len(Friendship.objects.all()) > 0:
			return Response(FriendshipSerializer(Friendship.objects.all(), many = True).data)
		else:
			return Response({"message" : " No Friendships yet"})

@api_view(['POST', 'GET'])
def unfriend(request):

	friend_username = request.DATA.get('user')

	try: 
		relation1 = Friendship.objects.get(user = request.user, friend__username = friend_username)
		relation2 = Friendship.objects.get(user__username = friend_username, friend = request.user)

		relation1.status = 4
		relation2.status = 4

		relation1.save()
		relation2.save()
	except:
		return Response(no_resource_error())

	return Response({"status": 0, "friendship": request.user.friendship_status(friend_username)})



# ensure that both are friends 
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


	
