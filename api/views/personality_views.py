from social.models import User, Friendslist, Friendship
from personality.models import Reputation, Review, ReviewDraft, TraityQuestion, Feedback
from social.serializers import UserSerializer, FriendslistSerializer, FriendshipSerializer
from personality.serializers import ReputationSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error

# make the user is friend of the logged in user
@api_view(['GET', 'POST'])
def reputation(request, uid):
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
				return Response({"message" : "Done"})
			except:
				return Response({"error": "DB error"})
		return friend_info(request, uid, cb)
	elif request.method == 'GET':
		def cb(friend, relation):
			try:
				repo = Reputation.objects.get(user = friend, friend = request.user)
				return Response(ReputationSerializer(repo).data)
			except Reputation.DoesNotExist:
				return Response(no_resource_error())

		return friend_info(request, uid, cb)


	

@api_view(['GET', 'POST'])
def review(request, uid):
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
				rev = Review(user = friend, friend = request.user, review  = review)
		
			try:
				rev.save()
			except:
				return Response({"error": "DB error"})

			rev_drf = ReviewDraft(review = rev, text = review)
			rev_drf.save()
		
			return Response({"message" : "ok"})
	
		return friend_info(request, uid, cb)
	elif request.method == 'GET':
		def cb(friend, relation):
			try:
				review = Review.objects.get(user = friend, friend = request.user)
				return Response(ReviewSerializer(review).data)
			except Review.DoesNotExist:
				return Response(no_resource_error())

		return friend_info(request, uid, cb)

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
def nick(request, uid):
	if request.method == "POST":
		def cb(friend, relation):
			try: 
				nick = request.DATA['nick'].lower()
			except:
				return Response({"error": "Query param required"})

			relation.nick = nick

			try:
				relation.save()
				return Response({"message": "ok"})
			except:
				return Response({"error": "Db error"})

		return friend_info(request, uid, cb)
	elif request.method == 'GET':
		def cb(friend, relation):
			if not relation.nick:
				return Response(no_resource_error())
			else:
				return Response({"nick": relation.nick})

		return friend_info(request, uid, cb)


@api_view(['GET', 'POST'])
def feedback(request, uid):
	if request.method == "POST":
		def cb(friend, relation):
			try:
				question_id = request.DATA['question']
				rating = int(request.DATA['rating'])
			except:
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
					return Response({"message": "ok"})
				except:
					return Response(db_error)

			except TraityQuestion.DoesNotExist:
				return Response(wrong_credentials_error())
		
		return friend_info(request, uid, cb)

@api_view(['GET'])
def my_reviews(request):
	if request.method == 'GET':
		user = request.user
		revs = user.myReviews.all()
		return Response(ReviewSerializer(revs, many = True).data)

@api_view(['GET'])
def my_nicks(request):
	if request.method == 'GET':
		user = request.user
		nicks = user.nicks()
		return Response(nicks)
def my_feedbacks(request):
	pass
