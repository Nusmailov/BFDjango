from django.db import models
from django.contrib.auth.models import User


class TaskManager(models.Model):
    def for_user(self, user):
        return self.filter(owner=user)


class Task(models.Model):
    name = models.CharField(max_length=100,default='name')
    title = models.CharField(max_length=100)
    created = models.DateTimeField()
    due = models.DateTimeField()
    object = TaskManager()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    mark = models.BooleanField()

    def to_json(self):
        return {
            'name': self.name,
            'id': self.id,
            'title': self.title,
            'owner': self.owner.username if self.owner else None,
            'created': self.created,
            'due': self.due,
            'mark': self.mark
        }


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def to_json(self):
        return {
            'name': self.name,
            'surname': self.surname
        }