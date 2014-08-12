from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(AbstractBaseUser):
	dob = models.DateField()


class Friendship(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	friend = models.ForeignKey(settings.AUTH_USER_MODEL)
	lists = models.ManyToManyField(Friendslist)
	category = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])
	nick = models.CharField(max_length=50, blank = True)

class Friendslist(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length = 50)

