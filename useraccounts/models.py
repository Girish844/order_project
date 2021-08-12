from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    email = models.CharField(max_length=100)


class user(models.Model):
    name = models.CharField(max_length=100)
    Uname = models.IntegerField(default=0)
    password = models.CharField(max_length=100)


class restaurants(models.Model):
    restaurants = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    restaurant_address = models.CharField(max_length=100)
    dishes = models.CharField(max_length=100)
    dishes_name = models.CharField(max_length=100)
    dishes_price = models.CharField(max_length=100)
    restaurants_in_which_dishes_are_avilable = models.CharField(max_length=100)
    orderplaced = models.CharField(max_length=100)
    user_who_placed_order = models.CharField(max_length=100)
    restaurant_from_which_order_is_placed = models.CharField(max_length=100)
    dishes_which_is_order = models.CharField(max_length=100)
    total_price = models.IntegerField(default=0)
    date = models.DateTimeField(max_length=100)

class userlogin(models.Model):
    restaurant=models.ForeignKey(restaurants,on_delete=models.CASCADE)

class architecture(models.Model):
    restro1 = models.CharField(max_length=100)
    restro2 = models.CharField(max_length=100)
    restro3 = models.CharField(max_length=100)
    restro4 = models.CharField(max_length=100)

class Article(models.Model):
    restro1 = models.CharField(max_length=100)
    restro2 = models.CharField(max_length=100)
    restro3 = models.CharField(max_length=100)
    restro4 = models.CharField(max_length=100)
class Sold(models.Model):
    Dishes=models.CharField(max_length=200)
    nosold=models.IntegerField()
    def __str__(self):
        return self.name
