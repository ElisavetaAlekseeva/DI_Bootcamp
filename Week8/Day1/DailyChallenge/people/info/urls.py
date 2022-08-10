from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('people', views.show_people, name='people'),
    path('person/<int:id>', views.get_person, name='person'),
]