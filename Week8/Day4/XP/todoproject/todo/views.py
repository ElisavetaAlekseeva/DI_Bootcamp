from django.shortcuts import render
from .models import Category_mod, ToDO_mod
from .forms import Category_form, ToDO_form
# Create your views here.

def add_todo(request):
    context = {'form':ToDO_form}

    if request.method == 'POST':
        form_filled = ToDO_form(request.POST)
        if form_filled.is_valid():
            title = form_filled.cleaned_data['title']
            details = form_filled.cleaned_data['details']
            deadline_date = form_filled.cleaned_data['deadline_date']
            category = form_filled.cleaned_data['category']
            ToDO_mod.objects.create(title=title, details=details, deadline_date=deadline_date, category=category)
    return render(request,'todo.html', context)


def add_cat(request):
    context = {'form':Category_form}
    if request.method == 'POST':
        form_filled = ToDO_form(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            image = form_filled.cleaned_data['image']
            Category_mod.objects.create(name=name, image=image)
    return render(request,'category.html', context)
        

def display_cat(request, id):
    cat = Category_mod.objects.get(id=id)
    todos = cat.todos.all()
    context = {'categoty':cat,'todos': todos}

    return render(request, 'display_cat.html', context)


def display_all(request):
    cat = Category_mod.objects.all()
    context = {'categories':cat}

    return render(request, 'display_all.html', context)