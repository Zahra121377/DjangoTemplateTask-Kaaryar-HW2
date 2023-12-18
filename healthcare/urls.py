
from django.urls import path
from .views import home, doctors,about

urlpatterns = [
    path('', home, name='home'),
    path('doctors', doctors, name='doctors'),
    path('about', about, name='about'),
]