from django.shortcuts import render
from .models import Car


def index(request):
    cars = Car.objects.all()
    for car in cars:
        car.stars = range(car.rating)  # Prepare the range here
    return render(request, 'car_dealer/index.html', )

def rent(request):
    cars = Car.objects.all()            
    return render(request, 'car_dealer/rent.html', )

def about(request):
    cars = Car.objects.all()
    return render(request, 'car_dealer/about.html', )

def contact(request):
    return render(request, 'car_dealer/contact.html')

