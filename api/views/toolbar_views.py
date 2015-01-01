from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from timeline.models import Post, Node, ThoughtDraft, Status, PostPrivacy,Comment, CommentDraft
from timeline.models import CommentCondemn, Rating
from api.helpers import create_parents, post_params_required, get_params_required
from timeline.serializers import PostPrivacySerializer
from datetime import datetime



@api_view(['GET'])
@get_params_required(['q'])
def search(request):


	if request.user.friends.count() < 0:
		return Response({"error": "You dont have any friends yet"})

	if request.method == "GET":
		q = request.GET.get('q')

		# print request.user.friends

		result = {}

		friends = [relation.friend.data_for_search() for relation in request.user.friends.filter(friend__firstname__icontains = q)]
		for friend in friends:
			result[friend['id']] = friend

		friends = [relation.friend.data_for_search() for relation in request.user.friends.filter(friend__lastname__icontains = q)]
		for friend in friends:
			result[friend['id']] = friend

		print result

		# return Response({"results" : result})

		return Response({"results": [result[key] for key in result], "status": 0})



