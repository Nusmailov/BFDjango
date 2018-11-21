from django.db import models
from main2.models import Student


class Pair(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    pair = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'email': self.email
        }

# Create your models here.
