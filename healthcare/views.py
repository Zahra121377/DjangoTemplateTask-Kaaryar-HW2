# Create your views here.
from django.shortcuts import render
from .models import Doctor
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})