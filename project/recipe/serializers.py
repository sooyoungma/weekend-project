from rest_framework import serializers
from recipe.models import Recipe, CalorieCount


class RecipeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Recipe
		fields = [ 'name_of_dish', 'serving_size']



class CalorieCountSerializer(serializers.ModelSerializer):

	class Meta
		model = CalorieCount
		fields = [ 'name_of_dish']