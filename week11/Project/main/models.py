from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(default="admin@gmail.com")
    def __str__(self):
        return self.name;


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    num_pages = models.IntegerField(default=100)
    def __str__(self):
        return self.title;


# Create your models here.
