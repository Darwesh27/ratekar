from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error


@api_view(['GET'])
def thoughts(request, username):
	data = {
		'text': "From thoughts",
		'next': None,
	}

	return Response(data);

@api_view(['GET'])
def photos(request, username):
	data = {
		'text': "From thoughts",
		'next': None,
	}

	return Response(data);

@api_view(['GET'])
def feedbacks(request, username):
	data = {
		'text': "From thoughts",
		'next': None,
	}

	return Response(data);

@api_view(['GET'])
def reviews(request, username):
	data = {
		'text': "From thoughts",
		'next': None,
	}

	return Response(data);
	
@api_view(['GET'])
def nicks(request, username):
	data = {
		'me': False,
		'text': "From thoughts",
		'next': None,
	}

	return Response(data);


@api_view(['GET'])
def comments(request, pid):

	data = {
		"comments": [
			{"text": "This is a comment"},
			{"text": "This is a comment"},
			{"text": "This is a comment"},
			{"text": "This is a comment"},
		],
	}

	return Response(data);
	
@api_view(['GET', 'POST'])
def my_nick(request, username):


	nick = request.DATA.get('nick', 'chotia');
	data = {
		"nick": nick,
	}

	return Response(data);

@api_view(['GET', 'POST'])
def my_review(request, username):

	defualt_review = "Dum is a super is awsome person" 
	defualt_review += " with really nice botha.. "


	review = request.DATA.get('review', defualt_review);
	data = {
		"review": review,
	}

	return Response(data);

@api_view(['GET'])
def suggest_nicks(request, username):

	data = [
		'Cho',
		'Chussar',
		'Chawal',
	]
	return Response(data);
