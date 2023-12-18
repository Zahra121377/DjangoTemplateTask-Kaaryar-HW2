from django.urls import path

from .views import about, doctors, home

urlpatterns = [
    path("", home, name="home"),
    path("doctors", doctors, name="doctors"),
    path("about", about, name="about"),
]
