from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ShopFlowerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class FlowerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = "__all__"


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password",)

