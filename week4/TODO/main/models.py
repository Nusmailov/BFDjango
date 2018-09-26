from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    due_on = models.DateTimeField(auto_now_add = False)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    mark = models.BooleanField(default = False)

    def __str__(self):
        return self.title