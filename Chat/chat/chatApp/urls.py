from django.urls import path
from .views import signup, signin, signout, profile, update_profile, friends


urlpatterns = [
    path('signup', signup, name='signup'),
    path('homepage', signin, name='signin'),
    path('signout', signout, name='signout'),
    path("update-profile", update_profile, name="update_profile"),
    path("user-profile", profile, name="profile"),
    path("friends/<str:pk>", friends, name="friends"),

]
