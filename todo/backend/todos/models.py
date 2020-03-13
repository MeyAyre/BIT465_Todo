from django.db import models


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
       default='available',)
    friendliness = models.IntegerField()
    trainability = models.IntegerChoices(max_length=5, choices=list(zip(range(1, 6), range(1, 6))), unique=True)
    shedding_amount = models.IntegerChoices(max_length=5, choices=list(zip(range(1, 6), range(1, 6))), unique=True)
    excercise_needs = models.IntegerChoices(max_length=5, choices=list(zip(range(1, 6), range(1, 6))), unique=True)