from contextlib import redirect_stderr
from unicodedata import name
from xml.dom.expatbuilder import FilterVisibilityController
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import ProfileForm
from .models import UserProfile



def signup(request):
    context = {'form': UserCreationForm}
    if request.method == 'POST':
        form_filled = UserCreationForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save(commit = False)

            username = form_filled.cleaned_data.get('username')
            password = form_filled.cleaned_data.get('password1')
            # Authentiacate
            user = authenticate(username=username, password=password)
            
            user = form_filled.save()

            UserProfile.objects.create(user_id = user.id)

            # regulars = Group.objects.get(name='Regulars')
            # regulars.user_set.add(user)

            login(request, user)
            return redirect('update_profile')

        else:
            return render(request, 'signup.html', {'form': form_filled})

    return render(request, 'signup.html', context)


def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            login(request, user)
        
        else:
            return render(request, 'homepage.html', {'form': AuthenticationForm(request.POST)})
    
    else:
        return render(request, 'homepage.html', {'form': AuthenticationForm})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('signin')


def update_profile(request):
    profile = request.user.userprofile
    form = ProfileForm(request.POST or None, instance=profile)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'update_profile.html', context)


def profile(request):
    user = request.user
    profile = User.userprofile
    context = {'profile': profile}

    return render(request, 'profile.html', context)