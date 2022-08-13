from distutils.command import upload
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Category_model, Gif_model
from .forms import Category_form, Gif_form
# Create your views here.

def create_category(request):


    if request.method == 'POST':
        form_filled = Category_form(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            Category_model.objects.create(name = name)

    context = {'form': Category_form}
    return render(request, 'create_category.html', context)


def create_gif(request):
    if request.method == 'POST':
        form_filled = Gif_form(request.POST)
        if form_filled.is_valid():
            title = form_filled.cleaned_data('title')
            url = form_filled.cleaned_data('url')
            uploader = form_filled.cleaned_data('uploader_name')
            categories = form_filled.cleaned_data('category')
            new_gif = Gif_model(title=title, url=url, uploader_name=uploader)
            new_gif.save()
            for cat in categories:
                new_gif.categories.add(cat)
            new_gif.save()
    
    context = {'form': Gif_form}

    return render(request, 'create_gif.html', context)


def category_view(request, id):
    category = Category_model.objects.get(id=id)
    gifs = category.gifs.all()

    context = {'category': category, 'gifs': gifs}
    return render(request, 'category.html', context)
    

def homepage(request):
    context = {'gifs': Gif_model.objects.all(),
                'categories': Category_model.objects.all()}
    return render(request, 'homepage.html', context)

