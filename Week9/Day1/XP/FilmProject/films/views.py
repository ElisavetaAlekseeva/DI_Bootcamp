from email import message
import imp
from django.shortcuts import render, redirect
from .forms import FilmForm, DirectorForm, ReviewForm
from .models import Director, Film, Review
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import generic
from django.db.models import Q
from itertools import chain


context = {'films': Film.objects.all(), 'directors': Director.objects.all()}

def homepage(request):
    context = {'films': Film.objects.all(), 'directors': Director.objects.all(), 'formIn':AuthenticationForm, 'formUp': UserCreationForm}
    return render(request, 'homepage.html', context)


def add_film(request):
    context.update({'form': FilmForm(initial='realeased_date')})

    if request.method == 'POST':
        form_field = FilmForm(request.POST)
        print('-------------')
        print(request.POST)
        print('-------------')
        if form_field.is_valid():
            print('ADDED')
            form_field.save()
            return redirect('homepage')
        else:
            print(form_field.errors)
            print('notADDED')
            context.update({'form': form_field})
            return render(request, 'add_film.html', context)


    return render(request, 'add_film.html', context)


def add_director(request):
    context.update({'form': DirectorForm})

    if request.method == 'POST':
        form_field = DirectorForm(request.POST)
        if form_field.is_valid():
            form_field.save()
            return redirect('homepage')
        else:
            print(form_field.errors)

    return render(request, 'add_director.html', context)

def director_films(request, id):
    director = Director.objects.get(id=id)
    films = director.films.all()
    context.update({'director': director,'films': films})
    return render(request, 'director_films.html', context)


def about_film(request, id):
    film = Film.objects.get(id=id)
    form = ReviewForm
    context = {'film':film, 'form': form}

    if request.method == 'POST':
        form_filled = ReviewForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('about_film')
            
    return render(request, 'about_film.html', context)

def update_director(request, id):
    dir = Director.objects.get(id=id)
    form = DirectorForm(request.POST or None, instance=dir)
    context.update({'form': form})
    if form.is_valid():
        form.save()
        # messages.add_message(reqwuest, message.SUCCESS, '')
        return redirect('homepage')
    return render(request, 'update_director.html', context)


def update_film(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST or None, instance=film)
    context.update({'form': form})
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, 'update_film.html', context)



def delete_film(request, id):
    film = Film.objects.filter(id=id)
    film.delete()
    return redirect('homepage')


def delete_director(request, id):
    director = Director.objects.filter(id=id)
    director.delete()
    return redirect('homepage')



def director_search(request):
    query_dict = request.GET
    try:
        query = query_dict.get('search')
    except:
        query = None

    if query is not None:
        directors = Director.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query))
        films = Film.objects.filter(Q(title__icontains = query))

    context = {'objects_selected': chain(directors,films)}

    return render(request, 'director_search.html', context)

