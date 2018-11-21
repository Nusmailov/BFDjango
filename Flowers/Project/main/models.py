from django.db import models


class Location(models.Model):
    street = models.CharField(max_length=100)
    block = models.IntegerField()


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=200)
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, default='')

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Basket(models.Model):
    flowers = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True)
    sum = models.ForeignKey(Flower, on_delete=models.CASCADE, blank=True)


class ShopFlower(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return self.id