# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Doctor


def home(request):
    try:
        template = loader.get_template("healthcare/index.html")
    except Exception as e:
        print(f"Error loading template: {e}")
        return HttpResponse("Error loading template")

    return HttpResponse(template.render())


def about(request):
    try:
        template = loader.get_template("healthcare/about.html")
    except Exception as e:
        print(f"Error loading template: {e}")
        return HttpResponse("Error loading template")

    return HttpResponse(template.render())


def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, "healthcare/doctor.html", {"doctors": doctors})
