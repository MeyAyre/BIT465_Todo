# todos/serializers.py
from rest_framework import serializers
from .models import Todo, Dog, Breed


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo

class BreedSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(choices=Breed.STATUS)
    
    class Meta:
        fields = (
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'shedding_amount',
            'excercise_needs',
        )
        model = Breed

class DogSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(
        queryset=Breed.objects.all(), 
        slug_field='name')

    class Meta:
        fields = (
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favorite_food',
            'favorite_toy',
        )
        model = Dog

