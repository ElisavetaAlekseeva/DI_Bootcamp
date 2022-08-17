from contextlib import redirect_stderr
from unicodedata import name
from xml.dom.expatbuilder import FilterVisibilityController
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import ProfileForm
from films.models import Director

directors = Director.objects.all()

def signup(request):
    context = {'form': UserCreationForm}

    if request.method == 'POST':
        form_filled = UserCreationForm(request.POST)

        if form_filled.is_valid():
            form_filled.save(commit=False)

            username = form_filled.cleaned_data.get('username')
            password = form_filled.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            user = form_filled.save()

            regulars = Group.objects.get(name='Regulars')
            regulars.user_set.add(user)

            login(request, user)
            return redirect('homepage')

        else:
            return render(request, 'signup.html', {'form': form_filled})

    else:
            return render(request, 'signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            login(request, user)
        
        else:
            return render(request, 'signin.html', {'form': AuthenticationForm(request.POST)})
    
    else:
        return render(request, 'signin.html', {'form': AuthenticationForm, 'directors': directors})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('signin')


def create_profile(request):

    if request.method == 'POST':
        filled_form = ProfileForm(request.POST)

        if filled_form.is_valid():
            profile = filled_form.save(commit = False)

            profile.user = request.user
            profile.save()

            return redirect('profile')

        else:
            return render(request, 'create_profile.html', {'form': filled_form})

    
    else:

        if request.user.is_authenticated:
            form = ProfileForm()
            return render(request, 'create_profile.html', {'form': form})
        else:
            return redirect('signin')