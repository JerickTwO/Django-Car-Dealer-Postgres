from django.shortcuts import render, get_object_or_404
from .models import Car


def index(request):
    cars = Car.objects.all()
    for car in cars:
        car.stars = range(car.rating)  # Prepare the range here
    return render(request, 'car_dealer/index.html', {'cars': cars})

def rent(request):
    cars = Car.objects.all()            
    return render(request, 'car_dealer/rent.html', {'cars': cars})

def about(request):
    cars = Car.objects.all()
    return render(request, 'car_dealer/about.html', {'cars': cars})

def contact(request):
    return render(request, 'car_dealer/contact.html')

