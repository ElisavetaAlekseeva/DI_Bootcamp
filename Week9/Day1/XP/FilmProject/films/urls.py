from django.urls import path
from .views import (homepage, add_film, add_director, update_film, update_director, director_films,about_film, delete_film, delete_director)

urlpatterns = [
    path('homepage', homepage, name='homepage'),
    path('add-film', add_film, name='add_film'),
    path('add-director', add_director, name='add_director'),
    path('update-film/<int:id>', update_film, name='update_film'),
    path('update-director/<int:id>', update_director, name='update_director'),
    path('director-films/<int:id>', director_films, name='director_films'),
    path('about-film/<int:id>', about_film, name='about_film'),
    path('delete-film/<int:id>', delete_film, name='delete_film'),
    path('delete-director/<int:id>', delete_director, name='delete_director'),
]
