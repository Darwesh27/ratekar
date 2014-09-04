from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, username, email, firstname, lastname, password = None):
		user = self.model(username = username, email = email, firstname = firstname, lastname = lastname)
		user.set_password(password)
		return user

	def create_superuser(self, username, email, firstname, lastname, password):
		user = self.create_user(username, email, firstname, lastname, password = password)
		user.save()
		return user


class User(AbstractBaseUser):
	firstname = models.CharField(max_length = 15)
	lastname = models.CharField(max_length = 15)
	username = models.CharField(max_length = 15, unique = True)
	email = models.EmailField(unique = True)
	phone_number = models.CharField(null=True, unique = True, max_length = 15)
	dob = models.DateField(null = True)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['firstname', 'lastname', 'email']

	@property
	def is_superuser(self):
		return self.is_staff

	def has_perm(self, perm, obj=None):
		return self.is_staff

	def has_module_perms(self, app_label):
		return self.is_staff

	def get_short_name(self):
		return self.firstname

	def get_full_name(self):
		return self.firstname + " " + self.lastname

	def is_friend_of(self, person):
		try:
			rel = Friendship.objects.get(user = self, friend = person)
			if rel.status == 3:
				return True
			else:
				return False

		except Friendship.DoesNotExist:
			return False

	def __unicode__(self):
		return self.get_full_name()





class Friendslist(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length = 50)



class Friendship(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friends')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendOf')
	lists = models.ManyToManyField(Friendslist)
	circle = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)], default = 2)
	nick = models.CharField(max_length=50, null = True)
	status = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)], default = 1)





