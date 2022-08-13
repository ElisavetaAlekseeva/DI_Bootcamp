from django.urls import path
from .views import (create_category, create_gif, homepage, category_view)

urlpatterns = [
    path('create_category', create_category, name='create_category'),
    path('create_gif', create_gif, name='create_gif'),
    path('homepage', homepage, name='homepage'),
    path('category/<int:id>', category_view, name='category'),
]
