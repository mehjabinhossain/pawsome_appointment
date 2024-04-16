from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)

#THIS


class Orders(models.Model):
    items=models.CharField(max_length=3000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    total = models.CharField(max_length=100)



class PetProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.IntegerField()



    #
    def __str__(self):
        return self.name


