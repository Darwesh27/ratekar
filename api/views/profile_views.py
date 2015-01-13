from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from api.helpers import create_parents, post_params_required, get_params_required
from api.helpers import fetch_user_posts
from api.helpers import paginate
from personality.models import *
from social.models import *




@api_view(['GET'])
def rankings(request):

	if request.method == "GET":

		friends = [rel.friend for rel in request.user.friends.filter(status = 3)]
		friends.append(request.user)

		return Response({"status": 0, "rankings": [friend.ranking(request.user) for friend in friends]})



@api_view(['GET'])
def get_review(request, rid):

	if request.method == "GET":


		try: 
			review = Review.objects.get(pk = rid)
		except Review.DoesNotExist:
			return Response(no_resource_error())


		if(review.user == request.user or review.friend == request.user):
			review = review.data(request.user)

			return Response({"review": review})
		else:
			return Response(unauthorized_error())
	else:
		return Response()


@api_view(['GET'])
# @login_required
def my_thoughts_rating(request):

	data = {
		"status" : 0,
		"rating" : request.user.thoughts_rating()
	}

	return Response(data)

@api_view(['GET'])
def thoughts(request, username):

	try: 
		user = User.objects.get(username = username)
	except: 
		return Response(no_resource_error())

	viewer = request.user 
	posts = []

	last = request.GET.get('last', None)
	order = request.GET.get('order', None)

	post_range = 5


	if last == None:
		posts = fetch_user_posts(owner = user, viewer = viewer, kind = 1, next = False)
	else:
		if order == 'old':
			posts = fetch_user_posts(owner = user, viewer = viewer, kind = 1, next = False, pid = last)
		elif order == 'new':
			posts = fetch_user_posts(owner = user, viewer = viewer, kind = 1, next = True, pid = last)



	next, previous = paginate(posts, request.path, post_range, last)


	data = {
		"items": posts,
		"status": 0,
		"next": next,
		"previous": previous,
	}

	return Response(data)


@api_view(['GET'])
def photos(request, username):
	data = {
		'text': "From thoughts",
		'next': None,
	}

	return Response(data);

@api_view(['GET'])
def feedbacks(request, username):

	try: 
		user = User.objects.get(username = username)
	except: 
		return Response(no_resource_error())


	data = {
		"items": user.feedbacks(request.user),
		"status": 0
	}

	return Response(data);

@api_view(['GET'])
def reviews(request, username):
	try: 
		user = User.objects.get(username = username)
	except: 
		return Response(no_resource_error())

	viewer = request.user 
	posts = []

	last = request.GET.get('last', None)
	order = request.GET.get('order', None)

	post_range = 5

	reviews = user.reviews(request.user, post_range, last)

	next, previous = paginate(reviews, request.path, post_range, last)

	data = {
		"items": reviews,
		"status": 0,
		"next": next,
		"previous": previous,
	}

	return Response(data);
	
@api_view(['GET'])
def nicks(request, username):

	try:
		friend = User.objects.get(username = username)
	except:
		return(no_resource_error())

	data = {}
	data['me'] = True if request.user == friend else False
	data['items'] = friend.nicks() if request.user == friend else []

	return Response(data);

