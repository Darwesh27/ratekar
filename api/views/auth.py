from social.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from social.serializers import UserSerializer, FriendslistSerializer, FriendshipSerializer

@api_view(['POST'])
def signup(request):
	try:
		username = request.DATA['username']
		firstname = request.DATA['firstname']
		lastname = request.DATA['lastname']
		email = request.DATA['email']
		password = request.DATA['password']
	except:
		return Response({"error" : "Query params required"})

	try:
		user = User(username = username, firstname = firstname, lastname = lastname, email = email)
		user.set_password(password)
		user.save()
	except:
		return Response({"error": "Cant create user"})
	
	user = authenticate(username=username ,password = password)
	
	login(request, user)

	return Response({"message" : "User created and logged in"})


@api_view(['POST'])
def signin(request):
	try:
		username = request.DATA['username']
		password = request.DATA['password']
	except:
		return Response({"error": "Query params required"})

	user = authenticate(username = username, password = password)

	if user:
		login(request, user)

		user_data = UserSerializer(request.user).data 
		user_data['reputation'] = request.user.repo()['repo']

		res = {
			"message": "User logged in",
			"user": request.user.profile()
		}
		return Response(res)
	else:
		return Response({"error": "Sorry can't Login"})


@api_view(['GET', 'POST'])
def signout(request):
	logout(request)
	return Response({"message": "logged out successfully"})
	

	
	


