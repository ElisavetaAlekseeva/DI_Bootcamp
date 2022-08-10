from django.urls import path,include
from django.contrib import admin
from .views import (get_by_name, get_by_number)


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('info/<str:name>', get_by_name, name = 'get_by_name'),
    path('number/<str:number>', get_by_number, name = 'get_by_number'),
    # path('', get_all, name = 'all')
]
