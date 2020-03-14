from django.contrib import admin

from .models import Todo, Breed, Dog

admin.site.register(Todo)
admin.site.register(Breed)
admin.site.register(Dog)