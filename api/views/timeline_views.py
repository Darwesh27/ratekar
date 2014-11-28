from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from timeline.models import Post, Node, ThoughtDraft, Status, PostPrivacy
from api.helpers import create_parents
from timeline.serializers import PostPrivacySerializer



@api_view(['GET', 'POST'])
def post_privacy(request):

	if request.user.post_privacy == None:
		p = PostPrivacy()
		p.save()
		request.user.post_privacy = p
		request.user.save()


	if request.method == 'POST':
		user = request.user
		level = request.DATA.get('level')

		if level == 3: 

			included = request.DATA.get('included', None)
			excluded = request.DATA.get('excluded', None)

			if included == None or excluded == None:
				return Response(query_error())

			valid_included = user.get_valid_lists(included)
			valid_excluded = user.get_valid_lists(excluded)

			privacy = user.post_privacy

			# First clear the previous selections
			privacy.include.clear()
			privacy.exclude.clear()

			for flist in valid_included:
				privacy.include.add(flist)

			for flist in valid_excluded:
				privacy.exclude.add(flist)

			privacy.save()

			return Response(PostPrivacySerializer(user.post_privacy).data)

		else:
			user.post_privacy.level = level
			user.post_privacy.save()
			return Response(PostPrivacySerializer(user.post_privacy).data)

	else:
		return Response(PostPrivacySerializer(request.user.post_privacy).data)






@api_view(['GET', 'POST'])
def post_status(request):
	"""
	"""
	# Check for required params first

	if request.method == 'POST':

		thought = request.DATA.get('thought', '')

		node = create_parents(owner = request.user, kind = 1, thought = thought)

		print node

		status = Status(node = node)
		status.save()

		return Response("oka")

	else:

		return Response([node.get_post(request.user) for node in Node.objects.all()])










