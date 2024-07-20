from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)  # Make
    year = models.IntegerField(default=0)  # Year
    image = models.ImageField(upload_to='car_images/')  # Image
    price = models.DecimalField(max_digits=30, decimal_places=2, default=0.00)  # Price
    seating_capacity = models.IntegerField(default=0)  # Seating capacity
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]
    transmission = models.CharField(
        max_length=50,
        choices=TRANSMISSION_CHOICES
    )  # Transmission
    miles = models.DecimalField(max_digits=10, decimal_places=2)  # Miles
    rating = models.IntegerField(default=0)  # Rating in stars

    def __str__(self):
        return f'{self.make} {self.year}'
