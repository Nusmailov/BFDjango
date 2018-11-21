from rest_framework import serializers
from main.models import Restaurant,City,Dish,Review,RestaurantReview,DishReview
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueValidator
import datetime


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=300)
#     email = serializers.EmailField()
#     is_staff = serializers.BooleanField()
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', )

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class CityModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    
    class Meta:
        model = City
        fields = ['id', 'name']

    def create(self, validated_data):
        city = City(**validated_data)
        city.save()
        return city


class RestaurantModelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=100)
    telephone = serializers.CharField(max_length=100)
    city = CityModelSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name','user','number','telephone','city']

    def create(self, validated_data):
        rest = Restaurant(**validated_data)
        rest.user=User.objects.first()
        rest.city = City.objects.first()
        rest.save()
        return rest

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


class DishModelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=100)
    telephone = serializers.CharField(max_length=100)
    city  = CityModelSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"

    def create(self, validated_data):
        rest = Restaurant(**validated_data)
        rest.user=User.objects.first()
        rest.city = City.objects.first()
        rest.save()
        return rest

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance