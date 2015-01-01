from social.models import User, Friendslist, Friendship
from personality.models import Reputation, Review, ReviewDraft, TraityQuestion, Feedback
from social.serializers import UserSerializer, FriendslistSerializer, FriendshipSerializer
from personality.serializers import ReputationSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from api.helpers import *

# make the user is friend of the logged in user
@api_view(['GET', 'POST'])
def reputation(request, username):
	if request.method == 'POST':
		def cb(friend, relation):
			try:
				reputation = int(request.DATA['reputation'])
			except:
				return Response({"error" : "Query Param required"})

			try:
				repo = Reputation.objects.get(user = friend, friend = request.user)
				repo.reputation = reputation
			except Reputation.DoesNotExist:
				repo = Reputation(user = friend, friend = request.user, reputation  = reputation)
		
			try:
				repo.save()
				return Response({"status": 0, "reputation": friend.repo(request.user)})
			except:
				return Response({"error": "DB error"})
		return friend_info(request, username, cb)
	elif request.method == 'GET':
		def cb(friend, relation):
			try:
				repo = Reputation.objects.get(user = friend, friend = request.user)
				return Response(ReputationSerializer(repo).data)
			except Reputation.DoesNotExist:
				return Response(no_resource_error())

		return friend_info(request, username, cb)


	

@api_view(['GET', 'POST'])
def review(request, username):
	if request.method == 'POST':
		def cb(friend, relation):
			try:
				review = request.DATA['review']
			except:
				return Response({"error" : "Query Param required"})

			try:
				rev = Review.objects.get(user = friend, friend = request.user)
				rev.review = review
			except Review.DoesNotExist:
				node = node_for_review(friend)
				rev = Review(user = friend, friend = request.user, node = node)
		
			try:
				rev.save()
			except:
				return Response({"error": "DB error"})

			rev_drf = ReviewDraft(review = rev, text = review)
			rev_drf.save()
		
			return Response(rev.data(request.user))
	
		return friend_info(request, username, cb)
	elif request.method == 'GET':
		def cb(friend, relation):
			try:
				review = Review.objects.get(user = friend, friend = request.user)
				return Response(review.data(request.user))
			except Review.DoesNotExist:
				return Response({"error": 1})

		return friend_info(request, username, cb)

@api_view(['POST'])
def like_review(request, rid):
	if request.method == 'POST':
		try:
			like = request.DATA['like']
		except:
			return Response(query_error())

		if not (type(like) == type(True)):
			return Response({"error": "like ni laga"})
		else:
			print like
	
		try: 
			rev = Review.objects.get(pk = rid)
			
			if rev.user == request.user:
				try:
					rev.like = like
					rev.save()
					print rev.like
					rev_drf = rev.reviewdraft_set.order_by('created_on')[0]
					rev_drf.like = like
					rev_drf.save()
					print rev_drf.like
					return Response({"message": "ok"})
				except:
					return Response(db_error())
			else:
				return Response(unauthorized_error())
		except Review.DoesNotExist:
			return Response(resource_error())


@api_view(['GET','POST'])
def nick(request, username):
	if request.method == "POST":
		def cb(friend, relation):
			try: 
				nick = request.DATA['nick']
			except:
				return Response({"error": "Query param required"})

			relation.nick = nick

			try:
				relation.save()
				return Response({"status": 0, "nick": relation.nick})
			except:
				return Response({"error": "Db error"})

		return friend_info(request, username, cb)
	elif request.method == 'GET':
		def cb(friend, relation):
			if not relation.nick:
				return Response(no_resource_error())
			else:
				return Response({"nick": relation.nick})

		return friend_info(request, username, cb)


@api_view(['GET', 'POST'])
def feedback(request, username):

	print request.method

	if request.method == "POST":
		def cb(friend, relation):
			try:
				question_id = request.DATA['id']
				rating = int(request.DATA['rating'])
			except:
				try:
					exclude = request.DATA['exclude']
					print exclude
					return Response({"feedback": friend.next_feedback(request.user, exclude = exclude)})
				except KeyError:
					print "Masla ho gya g"
					return Response(query_error())

			try:
				question = TraityQuestion.objects.get(pk = question_id)
				try:
					feedback = Feedback.objects.get(user = friend, friend = request.user, question = question)
				except Feedback.DoesNotExist:
					feedback = Feedback(user = friend, friend = request.user, question = question)
				
				feedback.rating = rating

				try:
					feedback.save()
					return Response({"message": "ok", "feedback": friend.next_feedback(request.user)})
				except:
					return Response(db_error)

			except TraityQuestion.DoesNotExist:
				return Response(wrong_credentials_error())
		
		return friend_info(request, username, cb)
	else:
		def cb(friend, relation):
			return Response({"feedback": friend.next_feedback(request.user)})

		return friend_info(request, username, cb)



@api_view(['POST'])
def new_feedback(request):
	if request.method == "POST":

		text = request.DATA.get("text")

		try: 
			old_question = TraityQuestion.objects.get(user = request.user, text__iexact = text)
			return Response({"error": 1, "status": 1, "message": "Already exists.."})
		except:

			if len(text) > 3:
				new_question = TraityQuestion(user = request.user, text = text, min_cat = 3)
				new_question.save()

				return Response({"status": 0})
			else:

				return Response({"status": 1, "error": 1})





