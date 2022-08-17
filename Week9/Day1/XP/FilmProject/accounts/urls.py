from django.urls import path
from .views import (signup, signin, signout, create_profile)

urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path('create-profile', create_profile, name='create_profile'),
    

]

