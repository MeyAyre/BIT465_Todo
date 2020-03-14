# todos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('dogs', views.DogList.as_view()),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),
    path('breeds', views.BreedList.as_view()),
    path('breeds/<int:pk>/', views.BreedDetail.as_view()),
]