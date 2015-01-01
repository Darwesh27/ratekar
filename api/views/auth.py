from social.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from social.serializers import UserSerializer, FriendslistSerializer, FriendshipSerializer
from api.errors import query_error

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

		res = {
			"message": "User logged in",
			"user": request.user.profile(request.user)
		}
		return Response(res)
	else:
		return Response({"error": "Sorry can't Login"})


@api_view(['GET', 'POST'])
def signout(request):
	logout(request)
	return Response({"message": "logged out successfully"})
	


@api_view(['GET', 'POST']) 
def check_username(request):
	username = request.DATA.get('username', '')

	res = {}

	if(username != ''): 
		users = User.objects.filter(username = username)

		if(len(users) > 0):
			res['exists'] = True
		else:
			res['exists'] = False

		return Response(res)
	else:
		return Response(query_error())


@api_view(['GET', 'POST']) 
def check_email(request):
	email = request.DATA.get('email', '')

	res = {}

	if(email != ''): 
		users = User.objects.filter(email = email)

		if(len(users) > 0):
			res['exists'] = True
		else:
			res['exists'] = False

		return Response(res)
	else:
		return Response(query_error())
	
	


