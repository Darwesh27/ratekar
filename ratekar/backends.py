# from django.conf import settings
from django.contrib.auth.models import check_password
from social.models import User

class CustomAuth(object):
    """
    """

    def authenticate(self, username=None, password=None):
    	try:
    		User.objects.get(email = username)

    		if user.check_password(password):
    			return User
    		else:
    			return None
    	except:
    		return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
