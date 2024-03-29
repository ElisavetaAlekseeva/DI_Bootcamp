from django.urls import path
from .views import (delete_message, friends, signup, signin, signout, 
                    profile, create_profile, 
                    chats, chat, sentMessage,
                    receivedMessage, chatNotification,
                    not_seen, friends, send_friend_request,
                    delete_friend_request, accept_friend_request,
                    decline_friend_request, delete_friend,
                    friendNotifications, notifications, send_message, get_last_message,
                    activate, delete_message)


urlpatterns = [
    path('signup', signup, name='signup'),
    path('', signin, name='signin'),
    path('signout', signout, name='signout'),
    path("create-profile", create_profile, name="create_profile"),
    path("user-profile/<int:pk>", profile, name="profile"),
    path("chats/<str:pk>", chats, name="chats"),
    path("chat/<str:pk>", chat, name="chat"),
    path("sent_message/<str:pk>", sentMessage, name="sent_message"),
    path('delete_message/<int:pk>/', delete_message, name='delete_message'),
    path("received_message/<str:pk>", receivedMessage, name="received_message"),
    path("not_seen/<str:pk>", not_seen, name="not_seen"),
    path("friends/<str:pk>", friends, name="friends"),
    path('send_friend_request/<int:pk>/', send_friend_request, name='send_friend_request'),
    path('delete_friend_request/<int:pk>/', delete_friend_request, name='delete_friend_request'),
    path('accept_friend_request/<int:pk>/', accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/<int:pk>/', decline_friend_request, name='decline_friend_request'),
    path('delete_friend/<int:pk>/', delete_friend, name='delete_friend'),
    path("chatNotification", chatNotification, name="chatNotification"),
    path("friendNotification", friendNotifications, name="friendNotifications"),
    path("notification", notifications, name="notifications"),
    path('send_message/<int:pk>', send_message, name="send_message"),
    path('get_last_message/<int:pk>', get_last_message, name='get_last_message'),
    path('activate/<uidb64>/<token>', activate, name='activate')
]
