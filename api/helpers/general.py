
def paginate(items, url,  items_range, last):

	next = None
	previous = None

	if(len(items) < items_range):
		if len(items) != 0:
			next = url + "?order=new&last=" + str(items[0]['id'])
		else: 
			if last != None:
				next = url + "?order=new&last=" + last
			else:
				next = url
	else: 
		previous = url + "?order=old&last=" + str(items[-1]['id'])

		next = url + "?order=new&last=" + str(items[0]['id'])


	return (next, previous) 


def handle_uploaded_file(f):

	from ratekar.settings import MEDIA_ROOT


	root = MEDIA_ROOT

	path = root + "/picture"

	print path

	with open(path, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)



