from unicodedata import name
from django.urls import path
from .views import (add_cat, add_todo, display_cat, display_all)

urlpatterns = [
    path('add_category',add_cat, name='add_category'),
    path('add_todo',add_todo, name='add_ctodo'),
    path('display_category/<int:id>',display_cat, name='category'),
    path('', display_all, name='display_all'),
]
