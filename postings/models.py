from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse



class Food(models.Model):
    food_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=100)

    def __str__(self):
       return str(self.food_id)+':'+self.food_name

class Meals(models.Model):
    meals_id = models.IntegerField(primary_key=True)
    foods =  models.ManyToManyField(Food)

    def __str__(self):
       return str(self.meals_id)

class Tasks(models.Model):
    
    Meals_and_Foods = models.ManyToManyField(Food)
    def __str__(self):
       return str(self.Meals_and_Foods)
















    

