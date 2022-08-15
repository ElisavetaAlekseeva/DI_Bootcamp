from django.shortcuts import render, redirect
from .forms import FilmForm, DirectorForm
from .models import Director, Film

context = {'films': Film.objects.all(), 'directors': Director.objects.all()}

def homepage(request):
    context = {'films': Film.objects.all(), 'directors': Director.objects.all()}
    return render(request, 'homepage.html', context)

def add_film(request):
    context.update({'form': FilmForm})

    if request.method == 'POST':
        form_field = FilmForm(request.POST)
        if form_field.is_valid():
            form_field.save()
            return redirect('homepage')
        else:
            print(form_field.errors)

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


def update_film(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(instance=film)
    context.update({'form': form})

    if request.method == 'POST':
        form_field = FilmForm(request.POST, instance=film)
        if form_field.is_valid():
            form_field.save()
            return redirect('homepage')
        else:
            return redirect('update_film', args=[id])

    return render(request, 'update_film.html', context)



def update_director(request, id):
    dir = Director.objects.get(id=id)
    form = DirectorForm(instance=dir)
    context.update({'form': form})

    if request.method == 'POST':
        form_field = FilmForm(request.POST, instance=dir)
        if form_field.is_valid():
            form_field.save()
            return redirect('homepage')
        else:
            return redirect('update_director', args=[id])

    return render(request, 'update_director.html', context)


def director_films(request, id):
    director = Director.objects.get(id=id)
    films = director.films.all()
    context.update({'director': director,'films': films})
    return render(request, 'director_films.html', context)

