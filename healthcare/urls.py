
from django.urls import path
from .views import doctors_list

urlpatterns = [
    path('', doctors_list, name='doctors-list'),
]