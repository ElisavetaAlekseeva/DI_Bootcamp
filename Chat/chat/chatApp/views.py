from calendar import c
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import ProfileForm, ChatForm
from .models import UserProfile, Friend, Chat
from itertools import chain
from django.contrib.auth import logout, login
from django.http import JsonResponse
import json


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Your Username is taken')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Your Email is taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = authenticate(username=username, password=password)
                login(request, user_login)

                user_model = User.objects.get(username=username)
                user_profile = UserProfile.objects.create(user=user_model)
                user_profile.save()
                return redirect('update_profile')

        else:
            messages.info(request, 'Password is Uncorrect')
            return redirect('signup')
    
    else: 
        return render(request, 'signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print('-----')
        print(user)

        if user is None:
            return redirect('signin')
        
        else:
            login(request, user)
            return redirect ('profile')
    
    else:
        return render(request, 'homepage.html', {'form': AuthenticationForm})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('signin')


@login_required(login_url='signin')
def profile(request):
    user = request.user
    user_profile = user.userprofile

    context = {'user': user, 'user_profile': user_profile}
    return render(request, 'profile/profile.html', context)


@login_required(login_url='signin')
def update_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile}

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.image
            hobbies = request.POST['hobbies']
            location = request.POST['location']

            user_profile.image = image
            user_profile.hobbies = hobbies
            user_profile.location = location
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            hobbies = request.POST['hobbies']
            location = request.POST['location']

            user_profile.image = image
            user_profile.hobbies = hobbies
            user_profile.location = location
            user_profile.save()
        
        return redirect('update_profile')

    return render(request, 'update_profile.html', context)
        

def friends(request, pk):
    user = request.user.userprofile
    friends = user.friends.all()


    context = {'friends': friends, 'user': user}

    return render(request, 'profile/friends.html', context)


def chat(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    form = ChatForm()
    user = request.user.userprofile
    profile = UserProfile.objects.get(id = friend.profile.id)
    chats = Chat.objects.all()
    received_chats = Chat.objects.filter(sender=profile, receiver=user, message_seen = False)
    received_chats.update(message_seen=True)

    if request.method == 'POST':
        form = ChatForm(request.POST)

        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = user
            chat.receiver = profile
            chat.save()

            return redirect('chat', pk = friend.profile.id)

    context = {'friend': friend, 'form': form, 
                'user': user, 'profile': profile,  
                'chats': chats, 'num': received_chats.count()}

    return render(request, 'profile/chat.html', context)


def sentMessage(request, pk):
    user = request.user.userprofile
    friend = Friend.objects.get(profile_id=pk)
    profile = UserProfile.objects.get(id=friend.profile.id)
    new_message = Chat.objects.create(sender = user,
                                    receiver = profile, message_seen = False)

    return JsonResponse(new_message.body, safe=False )


def receivedMessage(request, pk):
    user = request.user.userprofile
    friend = Friend.objects.get(profile_id=pk)
    profile = UserProfile.objects.get(id=friend.profile.id)
    messages = Chat.objects.filter(sender=profile, receiver=user)
    arr = []

    for message in messages:
        arr.append(message.body)

    return JsonResponse(arr, safe=False)


def not_seen(request, pk):
    user = request.user.userprofile
    friend = Friend.objects.get(profile_id=pk)
    profile = UserProfile.objects.get(id=friend.profile.id)
    messages = Chat.objects.filter(sender=profile, receiver=user, message_seen=False)

    message_list = [{
        "sender": message.sender.name,
        "message": message.body,

    } for message in messages]
    messages.update(message_seen=True)
    
    return JsonResponse(message_list, safe=False)


def chatNotification(request):
    user = request.user.userprofile
    friends = user.friends.all()
    arr = []

    for friend in friends:
        chats = Chat.objects.filter(sender__id=friend.profile.id, receiver=user, message_seen=False)
        arr.append(chats.count())

    return JsonResponse(arr, safe=False)
