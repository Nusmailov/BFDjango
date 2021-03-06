from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField( blank= True, null=True)
    phone = models.CharField(max_length=11)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)


class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class ShopFlower(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    flower_id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    price = models.IntegerField()


class Order(models.Model):
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    sum = models.IntegerField()


class OrderFlower(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    count = models.IntegerField()
