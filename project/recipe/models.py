from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Recipe(models.Model):
	name_of_dish = models.CharField(max_length=100)
	serving_size = models.DecimalField(max_digits=8, decimal_places=2)


class CalorieCount(models.Model):
	name_of_dish = models.ForeignKey(Recipe)