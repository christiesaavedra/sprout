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

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

class NestedRecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)
    photo = serializers.SerializerMethodField('photo_path')

    def photo_path(self, obj):
        # photo_url = ''.join(['https://', request.META['HTTP_HOST'], '/static/', photo_name])
        photo_url = ''.join(['http://localhost:8001/media/', obj.photo.name])
        return photo_url

    class Meta:
        model = Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe



#class RecipeNestedSerializer(serializer.ModelSerializer):
#        ingredients = IngredientSerializer(many=True)
# class AddressSerializer(serializers.ModelSerializer):
#     """Serializes an Address object"""
#     class Meta:
#         model = Address