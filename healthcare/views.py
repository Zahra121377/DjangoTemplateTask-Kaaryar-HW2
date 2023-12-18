# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Doctor

def home (request):
    try:
        template = loader.get_template('healthcare/index.html')
    except Exception as e:
        print(f"Error loading template: {e}")
        return HttpResponse("Error loading template")

    return HttpResponse(template.render())
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, "healthcare/doctor.html", {"doctors": doctors})
