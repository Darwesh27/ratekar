from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from timeline.models import Post, Node, ThoughtDraft, Status, PostPrivacy,Comment, CommentDraft
from timeline.models import CommentCondemn, Rating
from api.helpers import create_parents, post_params_required, get_params_required
from timeline.serializers import PostPrivacySerializer
from datetime import datetime



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

		data = {
			"post" : node.get_post(request.user),
			"status": 0
		}

		return Response(data)

	else:

		return Response([node.get_post(request.user) for node in Node.objects.all()])



@api_view(['POST'])
@post_params_required(['rating'])
def rate_post(request, pid):

	if request.method == "POST":


		try: 
			post = Node.objects.get(pk = pid)
		except:
			return Response(no_resource_error())


		if(request.user.can_rate(post)):
			post_rating, created = Rating.objects.get_or_create(node = post, friend = request.user)
			my_rating = request.DATA.get('rating')

			post_rating.rating = my_rating
			post_rating.save()

			return Response({"status": 0, "rating": post.rating(request.user)})

		else:
			return Response(unauthorized_error())


@api_view(['GET'])
def get_post(request, pid):

	if request.method == "GET":

		try: 
			post = Node.objects.get(pk = pid)
		except:
			return Response(no_resource_error())


		if(request.user.can_interact_with(post)):
			post = post.get_post(request.user)

			return Response({"post": post})
		else:
			return Response(unauthorized_error())
	else:
		return Response()


@api_view(['GET', 'POST'])
def stream(request):

	if request.method == 'GET':

		friends = [relation.friend for relation in request.user.my_friends().all()]

		friends.append(request.user)

		last = request.GET.get('last', None)
		order = request.GET.get('order', None)


		post_range = 5


		if last == None:
			posts = [post.node_set.all()[0].get_post(request.user) for post in Post.objects.filter(owner__in = friends).order_by('-time')[0:post_range]]
		else:
			if order == 'old':
				posts = [post.node_set.all()[0].get_post(request.user) for post in Post.objects.filter(owner__in = friends, id__lt = last).order_by('-time')[0:post_range]]
			elif order == 'new':
				posts = [post.node_set.all()[0].get_post(request.user) for post in Post.objects.filter(owner__in = friends, id__gt = last).order_by('-time')[0:post_range]]


		next = None
		previous = None


		if(len(posts) < post_range):
			if len(posts) != 0:
				next = request.path + "?order=new&last=" + str(posts[0]['id'])
			else: 
				next = request.path + "?order=new&last=" + last
		else: 
			previous = request.path + "?order=old&last=" + str(posts[-1]['id'])

			next = request.path + "?order=new&last=" + str(posts[0]['id'])


		status = 0


		data = {
			"posts": posts,
			"status": status,
			"next": next,
			"previous": previous,
		}

		return Response(data)


@api_view(['GET', 'POST'])
@post_params_required(['text'])
def add_comment(request, pid):

	if request.method == 'POST':

		text = request.DATA.get('text', '')

		try: 
			post = Node.objects.get(pk = pid)
		except Node.DoesNotExist:
			return Response(no_resource_error())

		if request.user.can_interact_with(post): 
			comment = Comment(node = post, friend = request.user)
			comment.save()


			commentDraft = CommentDraft(comment = comment, text = text)
			commentDraft.save()

			return Response({"comment": comment.data(request.user), "status": 0})

		else:
			return Response(unauthorized_error())

	else:
		return Response([comment.data(request.user) for comment in Comment.objects.all()])

@api_view(['GET', 'POST'])
def condemn_comment(request, cid):

	if request.method == 'POST':

		condemn = request.DATA.get('condemn', False)


		try: 
			comment = Comment.objects.get(pk = cid)
		except Comment.DoesNotExist:
			return Response(no_resource_error())


		post = comment.node


		if request.user.can_interact_with(post): 
			comment_condemn, created = CommentCondemn.objects.get_or_create(friend = request.user, comment = comment)

			if created:
				comment_condemn.condemned = condemn
				comment_condemn.save()
			else:
				comment_condemn.condemned = condemn
				comment_condemn.save()

		else:
			return Response(unauthorized_error())

		return Response({"status" : 0, "comment": comment.data(request.user)})

	else:
		return Response([{"f": condemn.friend.id, "c": condemn.condemned} for condemn in CommentCondemn.objects.all()])


@api_view(['GET'])
def comment_condemners(request, cid):

	if request.method == 'GET':

		try: 
			comment = Comment.objects.get(pk = cid)
		except Comment.DoesNotExist:
			return Response(no_resource_error())

		post = comment.node

		if request.user.can_interact_with(post): 

			condemners = [condemn.friend.name() for condemn in comment.commentcondemn_set.all()]

			return Response({"condemners": condemners, "status": 0})
		else:
			return Response(unauthorized_error())



@api_view(['GET'])
def comments(request, pid):

	if request.method == 'GET':

		try: 
			post = Node.objects.get(pk = pid)
		except:
			return Response(no_resource_error())

		pFTime = request.GET.get('pFTime', None)
		nFTime = request.GET.get('nFTime', None)
		prevId = request.GET.get('befPrev', None)
		nextId = request.GET.get('befNext', None)


		if request.user.can_interact_with(post):

			if pFTime == None and nFTime == None:
				comments = [comment.data(request.user) for comment in post.comment_set.all().order_by('-time')[0:3]]
			elif pFTime != None:
				comments = [comment.data(request.user) for comment in post.comment_set.filter(time__lte = pFTime, id__lt = prevId).order_by('-time')[0:2]]
			elif nFTime != None:
				comments = [comment.data(request.user) for comment in post.comment_set.filter(time__gte = nFTime, id__gt = nextId).order_by('-time')[0:2]]

		else:
			return Response(unauthorized_error())


		next = None
		previous = None
		befPrev = None
		befNext = None


		if pFTime == None and nFTime == None:
			com_range = 3
		else:
			com_range = 2


		if(len(comments) < com_range):
			if len(comments) != 0:
				next = comments[0]['time']
				befNext = comments[0]['id']
			else: 
				next = nFTime
				befNext = nextId
		else: 
			previous = comments[-1]['time']
			befPrev = comments[-1]['id']

			next =comments[0]['time']
			befNext = comments[0]['id']


		data = {
			"comments": comments,
			"next": next,
			"previous": previous,
			'befNext': befNext,
			'befPrev': befPrev,
		}

		return Response(data)

















