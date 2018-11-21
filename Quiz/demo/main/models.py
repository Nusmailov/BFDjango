from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from main.serializers import UserSerializer


class AdvertManager(models.Model):
    def for_user(self, user):
        return self.filter(owner=user)


class Advert(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'address': self.address,
            'description': self.description,
            'price': self.price,
            'owner': self.owner.username if self.owner else None
        }


class AdvertSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    owner = UserSerializer(read_only=True)

    def create(self, validated_data):
        advert = Advert(**validated_data)
        advert.owner = User.objects.first()
        advert.save()
        return advert;

    def update(self, instance, validated_data):
        instance.title = validated_data('title', instance.title)
        instance.save()
        return instance
