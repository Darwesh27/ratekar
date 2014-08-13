from django.shortcuts import render
from social.models import User, Friendslist, Friendship
from personality.models import Reputation, Review, TraityQuestion, Feedback


def friendship(request):
	# A new friendship relation 
	if request.method == "POST":
		#initialize a request 
	pass

def friendship_details(request, fid):
	# return the Nick name, rating, circle and lists 
	pass

def friendship_circle(request, uid):
	try: 
		friend = User.objects.get(pk = uid)[0]
	except User.DoesNotExist:
		return Response(""" Send some errorfull response""")

	try: 
		relation = Friendship.objects.get(user = request.user, friend = friend)[0]
	except Friendship.DoesNotExist:
		return Response(""" Send some errorfull response""")

	if request.method == 'PUT':
		"""
		relation.circle = request.POST['circle']
		"""
		relation.save()

		return Response({succes = True})
		

	elif request.method == 'GET':
		return Response({circle = relation.circle})

	pass

def friendship_list(request, uid):
	pass

def rating(request, uid):
	pass

def review(request, uid):
	pass

def feedback(request, uid, fbid):
	pass


def friendlist(request):
	pass

def friendlist_detail(request, pk):
	pass

