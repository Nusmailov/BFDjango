from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    telephone = models.IntegerField()
    city = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField()
    date = models.DateTimeField()


class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


# Create your models here.
