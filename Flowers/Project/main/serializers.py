from rest_framework import serializers
from .models import *


class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ShopModelSerializer(serializers.ModelSerializer):
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


class BasketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "_all__"
