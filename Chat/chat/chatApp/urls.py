from django.urls import path
from .views import (signup, signin, signout, 
                    profile, update_profile, 
                    friends, chat, sentMessage,
                    receivedMessage, chatNotification)


urlpatterns = [
    path('signup', signup, name='signup'),
    path('homepage', signin, name='signin'),
    path('signout', signout, name='signout'),
    path("update-profile", update_profile, name="update_profile"),
    path("user-profile", profile, name="profile"),
    path("friends/<str:pk>", friends, name="friends"),
    path("chat/<str:pk>", chat, name="chat"),
    path("sent_message/<str:pk>", sentMessage, name="sent_message"),
    path("received_message/<str:pk>", receivedMessage, name="received_message"),
    path("chatNotification", chatNotification, name="chatNotification"),
]
