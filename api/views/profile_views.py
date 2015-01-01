from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from api.helpers import create_parents, post_params_required, get_params_required
from api.helpers import fetch_user_posts
from api.helpers import paginate
from social.models import *




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

	
@api_view(['GET', 'POST'])
def suggest_nicks(request, username):

	if request.method == 'POST':

		try:
			friend = User.objects.get(username = username)
		except:
			return(no_resource_error())

		if friend.is_friend_of(request.user):
			text = request.DATA.get('text', '')

			if len(text) > 3:
				relations = friend.friends.filter(nick__istartswith = text)

				if relations.count > 0:
					data = [stat['nick'] for stat in relations.values('nick').annotate()]
			else:
				return Response([])

		else:
			return Response(unauthorized_error())

		return Response(data);

	else:
		return Response([])


# @api_view(['GET', 'POST'])
# def feedback(request, username):

# 	feedbacks = [
# 		{
# 			'id': 0,
# 			'text': "Punctual",
# 			'rating': None,
# 		},
# 		{
# 			'id': 1,
# 			'text': "Looks nice in Long hair..",
# 			'rating': None,
# 		},
# 		{
# 			'id': 2,
# 			'text': "Keeps his promise..",
# 			'rating': None,
# 		},
# 	]

# 	feedback = request.DATA.get('feedback', feedbacks[0])

# 	feedback = feedbacks[(feedback['id'] + 1)%2]


# 	return Response(feedback);


@api_view(['GET', 'POST']) 
# @post_params_required(['exclude'])
def friend_suggestions(request):

	friends = [relation.friend for relation in request.user.my_friends()]
	print friends 

	final = {}

	for friend in friends:
		if request.method == 'POST':
			exclude = request.DATA.get('exclude')
			print exclude
			ff = [relation.friend for relation in friend.friends.exclude(friend = request.user).exclude(friend__in = friends).exclude(friend__username__in = exclude)]
		else:
			ff = [relation.friend for relation in friend.friends.exclude(friend = request.user).exclude(friend__in = friends)]

		for f in ff:
			if request.user.friends.filter(friend = f).exclude(status = 4).count == 0:
				if f.id in final:
					final[f.id]['count'] += 1
				else:
					final[f.id] = {}
					final[f.id]['count'] = 1
					final[f.id]['friend'] = f

	import operator

	result = [l['friend'].data_for_post() for l in sorted(final.values(), key = operator.itemgetter('count'))]


	if request.method == "POST":
		result = result[0:1]

	return Response(result)










