from api.errors import db_error, query_error, no_resource_error, unauthorized_error
from rest_framework.response import Response
from functools import wraps


def get_params_required(params):
    """
    Check that the params are provided
    """

    def _dec(view_func):
        def _view(request, *args, **kwargs):

            # if not request.method == "GET":
            #     return view_func(request, *args, **kwargs)


        	for param in params: 
        		if not (param in request.GET):
        			return Response(query_error())

        	return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    return _dec

def post_params_required(params):
    """
    Check that the params are provided
    """

    def _dec(view_func):
        def _view(request, *args, **kwargs):

            # if request.method != "POST":
            #     return view_func(request, *args, **kwargs)

        	for param in params: 
        		if not (param in request.DATA):
        			return Response(query_error())

        	return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    return _dec


