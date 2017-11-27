from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

import requests




from recipe.models import Recipe, CalorieCount
from recipe.serializers import (
	RecipeSerializer, CalorieCountSerializer
)

class RecipeListView(generics.ListCreateAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer

	def perform_create(self, serializer):
		serializer.save()


class CalorieCountView(generics.ListCreateAPIView):
	queryset = CalorieCount.objects.all()
	serializer_class = CalorieCountSerializer






