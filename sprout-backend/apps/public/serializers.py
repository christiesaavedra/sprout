from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializes a User object"""
    class Meta:
        model = User
        fields = ('id', 'username')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe

#class RecipeNestedSerializer(serializer.ModelSerializer):
#        ingredients = IngredientSerializer(many=True)
# class AddressSerializer(serializers.ModelSerializer):
#     """Serializes an Address object"""
#     class Meta:
#         model = Address