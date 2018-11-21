from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class StudentManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Student(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = StudentManager()

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'user': self.created_by.username if self.created_by else None
        }

    def get_absolute_url(self):
        return reverse_lazy('main2:student/student_list')



class TeacherManager(models.Manager):
    def for_user(self,user):
        return self.filter(created_by=user)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = TeacherManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('main2:student_list')

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'user':self.created_by.username if self.created_by else None
        }

# Create your models here.
