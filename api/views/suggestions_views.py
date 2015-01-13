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
