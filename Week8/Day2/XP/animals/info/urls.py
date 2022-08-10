from django.urls import path
from .views import show_animals, get_by_animal_id, get_by_family_id

urlpatterns = [
    path('family/<int:id>', get_by_family_id, name='get_by_family_id'),
    path('animal/<int:id>', get_by_animal_id, name='get_by_animal_id'),
    path('animals/',show_animals,name='show_animals'),
]

