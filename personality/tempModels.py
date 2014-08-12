from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from social.models import Friendship

class Reputation(models.Model):
	relation = models.OneToOneField(Friendship)
	reputation = models.IntegerField(required=True, validators = [MinValueValidator(1), MaxValueValidator(10)])

	created_on = models.DateField(auto_now_add = True)
	updated_on = modesl.DateField(auto_now = True)

class Review(models.Model):
	relation = models.OneToOneField(Friendship)
	review = models.CharField(max_length = 200)
	liked = models.BooleanField(default = False)

	created_on = models.DateField(auto_now_add = True)
	updated_on = modesl.DateField(auto_now = True)

class Trait(models.Model):
	title  = models.CharField(max_length = 15)
	description  = models.CharField(max_length = 100)

class TraityQuestion(models.Model):
	trait = models.ForeignKey(Trait)
	text = models.CharField(max_lenght = 100)
	min_cat = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])

class Feedback(models.Model):
	relation = models.ForeignKey(Friendship)
	question = models.ForeignKey(TraityQuestion)
	rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])




