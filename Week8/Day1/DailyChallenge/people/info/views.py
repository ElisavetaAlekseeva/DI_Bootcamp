from django.shortcuts import render
import json
from django.http import HttpResponse
from tkinter.font import families
# Create your views here.


# def show_family(request,id):
#     family_selected = None
#     for family in families:
#         if family['id'] == id:
#             family_selected = family
#     return render(request, 'family.html', family_selected)

with open('info/data.json', 'r') as f:
    data = json.load(f)

people = data['people']


def show_people(request):

    context = {'people': people}
    context['people'].sort(key=lambda person: person['age'])

    return render(request, 'people.html',context)


def get_person(request, id):

    for person in people:
        if id == person['id']:
            return render(request, 'person.html', {'person': person})
    return HttpResponse(f'Theres no person with id {id}')
