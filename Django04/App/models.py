from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()


    class Meta:
        abstract = True

# Create your models here.
class Dog(Animal):
    bark = models.CharField(max_length=40)



class Cat(Animal):
    sleep = models.CharField(max_length=40)
