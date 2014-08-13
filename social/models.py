from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(AbstractBaseUser):
	firstname = models.CharField(max_length = 15)
	lastname = models.CharField(max_length = 15)
	username = models.CharField(max_length = 15, unique = True)
	email = models.EmailField(unique = True)
	phone_number = models.CharField(null=True, unique = True, max_length = 15)
	dob = models.DateField(null = True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['firstname', 'lastname', 'email']

class Friendslist(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length = 50)



class Friendship(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friends')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendOf')
	lists = models.ManyToManyField(Friendslist)
	category = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])
	nick = models.CharField(max_length=50, null = True)
