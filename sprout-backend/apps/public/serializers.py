from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializes a User object"""
    class Meta:
        model = User
        fields = ('id', 'username')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe


# class AddressSerializer(serializers.ModelSerializer):
#     """Serializes an Address object"""
#     class Meta:
#         model = Address