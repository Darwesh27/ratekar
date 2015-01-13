from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.utils import user_info, friend_info
from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from api.helpers import create_parents, post_params_required, get_params_required
from api.helpers import fetch_user_posts
from api.helpers import paginate, handle_uploaded_file 
from personality.models import *
from social.models import *



@api_view(['POST'])
def places(request):

	if request.method == "POST":
		names = request.DATA.get("places", None)

		print names

		for name in names:
			if len(name) > 3:
				try:
					place = Place.objects.get(name = name)
				except:
					place = Place(name = name)


				if place.employees:
					place.employees += 1
				else: 
					place.employees = 1
				place.save()

				try:
					request.user.places.add(place)

					request.user.save()
				except:
					return Response(db_error())


				print "done with %s " % name
			else:
				return Response({"error": "Name of place should be alteast 3 characters long."})

		return Response({"status": 0})




@api_view(['POST'])
def upload_profile(request):
	if request.method == 'POST':

		picture = request.FILES.get('picture', None)

		if picture: 
			request.user.profile_pic = picture

			request.user.save()

			return Response({"status": 0, "url": request.user.profile_pic.url})

		else:
			return Response(query_error())



@api_view(['GET', 'POST'])
def suggest_address(request):
	
	address = request.DATA.get('address', None)

	if address:
		locations = Location.objects.filter(address__icontains = address).values('address', 'residents')
		import operator

		result = [l['address'] for l in sorted(location.values(), key = operator.itemgetter('residents'))]

		return Response({"status": 0, "locations": result})
	else:
		return Response(query_error())


@api_view(['GET', 'POST'])
def suggest_place(request):

	name = request.DATA.get('name', None)

	if name:
		places = Place.objects.filter(name__icontains = address).values('name', 'people')
		import operator

		result = [l['name'] for l in sorted(places.values(), key = operator.itemgetter('people'))]

		return Response({"status": 0, "places": result})
	else:
		return Response(query_error())

@api_view(['GET', 'POST'])
def address(request):
	address = request.DATA.get('address', None)

	if address and len(address) > 3:

		try:
			location = Location.objects.get(address = address)
		except:
			location = Location(address = address)


		if request.user.home != None:
			request.user.home.residents -= 1

		request.user.home = location

		if location.residents:
			location.residents += 1
		else:
			location.residents = 1
		location.save()
		request.user.save()

		# Send the response back


	else:
		return Response(query_error())


@api_view(['GET', 'POST'])
def place(request):

	name = request.DATA.get('name', None)

	if name and len(name) > 3:

		try:
			place = Place.objects.get(name = name)
		except:
			place = Place(name = name)


		if request.user.work != None:
			request.user.work.employees -= 1

		request.user.work = place

		if place.employees:
			place.employees += 1
		else:
			place.employees = 1

		place.save()
		request.user.save()



