from multiprocessing import context
from django.shortcuts import render
from .models import Family, Animal
from django.http import HttpResponse
# Create your views here.


def get_by_family_id(request, id):
    family = Family.objects.get(id = id)
    family_animals = Animal.objects.filter(id=id)
    context = {
        'family': family,
        'animals': family_animals
    }
    return render(request, 'family.html', context)

def get_by_animal_id(request, id):
    animal = Animal.objects.get(id = id)
    return render(request, 'animal.html', {'animal':animal})

def show_animals(request):
    animal = Animal.objects.all()
    return render(request, 'animals.html', {'animal':animal})
