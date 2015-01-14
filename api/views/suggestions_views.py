from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from personality.models import *
from social.models import *


@api_view(['POST'])
def suggest_places(request):
	if request.method == "POST":
		text = request.DATA.get('text', None)

		if text:

			places = Place.objects.filter(name__iexact = text).order_by('-employees')

			if places.count() < 1:
				print "No exact Match found.."
				places = Place.objects.filter(name__istartswith = text).order_by('-employees')

			if places.count() < 1:
				print "No startswith Match found.."
				places = Place.objects.filter(name__icontains = text).order_by('-employees')

			if places.count() < 1:
				print "No contains Match found.."
				return Response({"status": 0, "places": []})
			else:
				return Response({"status": 0, "places": [places[0].name]})
		else:
			return Response(query_error())

@api_view(['GET', 'POST']) 
# @post_params_required(['exclude'])
def friend_suggestions(request):

	friends = [relation.friend for relation in request.user.my_friends()]
	print friends 

	final = {}

	for friend in friends:
		if request.method == 'POST':

			# People that have been already sent
			exclude = request.DATA.get('exclude')
			ff = [relation.friend for relation in friend.my_friends().exclude(friend = request.user).exclude(friend__in = friends).exclude(friend__username__in = exclude)]
		else:
			ff = [relation.friend for relation in friend.my_friends().exclude(friend = request.user).exclude(friend__in = friends)]

		for f in ff:
			if request.user.friends.filter(friend = f).exclude(status = 4).count == 0:
				if f.id in final:
					final[f.id]['count'] += 1
				else:
					final[f.id] = {}
					final[f.id]['count'] = 1
					final[f.id]['friend'] = f
					final[f.id]['close'] = True if f.places.filter(id__in = [place.id for place in request.user.places.all()]).count() > 0 else False

	# users = User.objects.all()

	# final = []

	# for user in users:
	# 	if user.username == "dum":
	# 		final.append({'close': True, 'count': 2, 'friend': user})
	# 	elif user.username == "test":
	# 		final.append({'close': True, 'count': 1, 'friend': user})
	# 	elif user.username == "admin":
	# 		final.append({'close': False, 'count': 3, 'friend': user})


	import operator

	def data_for_suggestion(stat):
		data = stat['friend'].data_for_post()
		data['common'] = stat['count']

		return data

	result = [data_for_suggestion(l) for l in sorted(final.values(), key = operator.itemgetter('close', 'count'), reverse = True)]

	# No more mutual friends wale friends
	if len(result) < 5:
		remain = 5 - len(result) 
		users_data = [user.data_for_post() for user in User.objects.exclude(
			id = request.user.id).exclude(
			id__in = [relation.friend.id for relation in request.user.friends.all()]).filter(
			places__name__in = [place.name for place in request.user.places.all()]).distinct()[0:remain]]

		for user_data in users_data:
			user_data['common'] = None

			result.append(user_data)

	next = True

	if request.method == "POST":

		for_pane = request.DATA.get('forPane', None)
		if for_pane:
			result = result[0:1]
		else:
			if len(result) > 5: 
				next = True
			else:
				next = False
			result = result[0:5]
	else:
		if len(result) < 5:
			next = False
		result = result[0:5]


	data = {
		'suggestions': result,
		'next': next,
		'status': 0
	}


	return Response(data)

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
