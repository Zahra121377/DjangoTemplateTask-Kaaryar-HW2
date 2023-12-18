
from django.urls import path
from .views import home, doctors_list

urlpatterns = [
    path('', home, name='home'),
    path('doctors', doctors_list, name='doctors-list'),
]