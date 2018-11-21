from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='restaurants')
    orders = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return "{}({})".format(self.name, self.city)


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return "{}({})".format(self.name, self.description)


class Review(models.Model):
    price = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}:{}".format(self.date, self.comment)


class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant_reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='restaurant_reviews')

    def __str__(self):
        return "{}:{}".format(self.user, self.review)


class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dishes_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dishes_reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='dishes_reviews')


class Order (models.Model):
    pass