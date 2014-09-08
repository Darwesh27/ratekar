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
			friend_id = request.DATA['user']
			circle = int(request.DATA['circle'])
		except:
			return Response({'error': 'Query params required'})

		try:
			friend = User.objects.get(pk = friend_id)
		except User.DoesNotExist:
			return Response({error: "No such user"})

		if friend == request.user:
			return Response({"error": "Fuck off"})


		try:
			old = Friendship.objects.get(user = request.user, friend = friend)
			#old = old[0]
			old_req = Friendship.objects.get(user = friend, friend = request.user)

			if old.status == 1:
				print "1"
				if old_req and old_req.status == 2:
					old.status = 3
					old.save()

					old_req.status = 3
					old_req.save()

					return Response({"message" : "Request Accepted"})
				
				elif old_req and old_req.status == 1:
					old.status = 2
					old.save()
					return Response({"message" : "Request Accepted"})
			else: 
				return Response({"error" : "Fuck off"})
		except Friendship.DoesNotExist:
		# Not an old friendship
			try:
				req = Friendship.objects.get(user = friend, friend = request.user)
				req = req[0]
				if req.status == 1:
					new_fs = Friendship(user = request.user, friend = friend, circle = circle)
					return Response({"message" : "Request Accepted"})
			except: 
			# Its a request
				new_req = Friendship(user = request.user, friend = friend, circle = circle, status = 2)
				new_req.save()

				new_res = Friendship(user = friend, friend = request.user)
				new_res.save()
				return Response({"message" : "Request sent"})
	
	elif request.method == 'GET':
		if len(Friendship.objects.all()) > 0:
			return Response(FriendshipSerializer(Friendship.objects.all(), many = True).data)
		else:
			return Response({"message" : " No Friendships yet"})


# ensure that both are friends 
@api_view(['GET'])
def friendship_details(request, fid):
	fid = int(fid)
	try:
		serializer = FriendshipSerializer(Friendship.objects.get(pk = fid))
		return Response(serializer.data)
	except Friendship.DoesNotExist:
		return Response({"error": "No such relation"})

@api_view(['GET', 'PUT'])
def friendship_circle(request, uid):
	if request.method == 'PUT':
		def cb(friend, relation):
			try: 
				circle = request.DATA['circle']
			except:
				return Response({"error": "Query param required"})
	
			relation.circle = circle
	
			try:
				relation.save()
				return Response({"message": "ok"})
			except:
				return Response({"error": "Db error"})
		
		return user_info(request, uid, cb)
	elif request.method == "GET":
		return Response({"error": "Abi ni bacha..!!"})

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
		return Response(FriendslistSerializer(Friendslist.objects.all(), many=True).data)

@api_view(['GET'])
def profile(request, username):
	if request.method == 'GET':
		def cb(friend, relation):
			user = relation.user
			usr = UserSerializer(user).data
			
			repo = user.repo()
			print repo
			usr['repo'] = repo['repo']

			return Response(usr)

		try:
			print username
			frnd = User.objects.get(username = username.lower())
			print frnd.id
			return friend_info(request, frnd.id, cb)
		except User.DoesNotExist:
			return Response(no_resource_error())


		
	
	
