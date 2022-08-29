from django.urls import path
from .views import (friends, signup, signin, signout, 
                    profile, update_profile, 
                    chats, chat, sentMessage,
                    receivedMessage, chatNotification,
                    not_seen, friends, send_friend_request,
                    delete_friend_request, accept_friend_request,
                    decline_friend_request, delete_friend)


urlpatterns = [
    path('signup', signup, name='signup'),
    path('homepage', signin, name='signin'),
    path('signout', signout, name='signout'),
    path("update-profile", update_profile, name="update_profile"),
    path("user-profile/<int:pk>", profile, name="profile"),
    path("chats/<str:pk>", chats, name="chats"),
    path("chat/<str:pk>", chat, name="chat"),
    path("sent_message/<str:pk>", sentMessage, name="sent_message"),
    path("received_message/<str:pk>", receivedMessage, name="received_message"),
    path("not_seen/<str:pk>", not_seen, name="not_seen"),
    path("chatNotification", chatNotification, name="chatNotification"),
    path("friends/<str:pk>", friends, name="friends"),
    path('send_friend_request/<int:pk>/', send_friend_request, name='send_friend_request'),
    path('delete_friend_request/<int:pk>/', delete_friend_request, name='delete_friend_request'),
    path('accept_friend_request/<int:pk>/', accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/<int:pk>/', decline_friend_request, name='decline_friend_request'),
    path('delete_friend/<int:pk>/', delete_friend, name='delete_friend'),
]
