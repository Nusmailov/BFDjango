from rest_framework import serializers
from main.models import TaskManager,Task
from django.contrib.auth.models import User
from main.models import Teacher
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueValidator
import datetime


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    class Meta:
        model = User
        fields = "__all__"


class TaskModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    owner = UserSerializer(read_only=True)

    def create(self, validated_data):
        task = Task(**validated_data)
        task.owner = User.objects.first()
        task.save()
        return task;

    def update(self, instance, validated_data):
        instance.name = validated_data('name', instance.name)
        instance.save()
        return instance


class TeacherModelSerializer(serializers.Serializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = "__all__"

