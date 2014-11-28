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


	nick = request.DATA.get('nick', 'Dummy');
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


@api_view(['GET', 'POST'])
def feedback(request, username):

	feedbacks = [
		{
			'id': 0,
			'text': "Punctual",
			'rating': None,
		},
		{
			'id': 1,
			'text': "Looks nice in Long hair..",
			'rating': None,
		},
		{
			'id': 2,
			'text': "Keeps his promise..",
			'rating': None,
		},
	]

	feedback = request.DATA.get('feedback', feedbacks[0])

	feedback = feedbacks[(feedback['id'] + 1)%2]


	return Response(feedback);


@api_view(['GET', 'POST']) 
def friend_suggestions(request):

	if request.method == "POST":
		print request.DATA['exclude']

		return Response({
			"name": "New",
			"imgUrl": "/static/img/mj2.jpg",
			"rating": 4.3,
			"mutual": 5,
			"username": "new",
		})

	data = [
		{
			"name": "Rafaqat Ali Raali",
			"imgUrl": "/static/img/mj2.jpg",
			"rating": 4.3,
			"mutual": 5,
			"username": "raali",
		},
		{
			"name": "Ali Masood",
			"imgUrl": "/static/img/mj2.jpg",
			"rating": 5.8,
			"mutual": 5,
			"username": "ali",
		},
		{
			"name": "Kamil Khitab",
			"imgUrl": "/static/img/mj2.jpg",
			"rating": 9.6,
			"mutual": 5,
			"username": "kamil",
		},
		{
			"name": "Malik Junaid",
			"imgUrl": "/static/img/mj2.jpg",
			"rating": 6.8,
			"mutual": 5,
			"username": "darwesh",
		},
	]

	return Response(data);








