from django.urls import path
from .views import show_animals, show_family

urlpatterns = [
    path('family/<int:id>', show_family, name='show_family'),
    path('animal/<int:id>', show_animals, name='show_animals'),

]
