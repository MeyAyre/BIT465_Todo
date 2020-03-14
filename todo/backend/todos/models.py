from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxLengthValidator

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed',on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=200)
    favorite_toy = models.CharField(max_length=200)

class Breed(models.Model):
    STATUS = (
       ('tiny', _('Tiny')),
       ('small', _('Small')),
       ('medium', _('Medium')),
       ('large', _('Large'))
    )
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=32,
       choices=STATUS,
       default='medium',)
    friendliness = models.IntegerField(
    choices=list(zip(range(1, 6), range(1, 6))), 
    unique=True,)
    trainability = models.IntegerField(
    choices=list(zip(range(1, 6), range(1, 6))), 
    unique=True,)
    shedding_amount = models.IntegerField(
    choices=list(zip(range(1, 6), range(1, 6))), 
    unique=True,)
    excercise_needs = models.IntegerField(
    choices=list(zip(range(1, 6), range(1, 6))), 
    unique=True,)