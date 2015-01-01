from django.shortcuts import render, render_to_response

def index(request):
	if(request.user.id):
		data = request.user.profile(request.user)
		return render(request, 'api/index.html', {'data': data})
	else:
		return render(request, 'api/index.html')


