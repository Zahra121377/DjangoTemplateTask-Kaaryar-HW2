
from django.urls import path
from .views import home, doctors

urlpatterns = [
    path('', home, name='home'),
    path('doctors', doctors, name='doctors'),
    path('about', doctors, name='about'),
]