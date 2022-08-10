from django.shortcuts import render
from .models import Person
from django.http import HttpResponse
# Create your views here.


def get_by_name(request, name):
    person = Person.objects.get(name = name)
    return render(request, 'info.html', {'person':person})

def get_by_number(request, number):
    person = Person.objects.get(phone_number = number)
    return render(request, 'info.html', {'person':person})



