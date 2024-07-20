from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)  # Marca del coche
    year = models.IntegerField(default=2024)  # Año del coche
    image = models.ImageField(upload_to='car_images/')  # Imagen del coche
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Precio del coche
    seating_capacity = models.IntegerField(default=0)  # Capacidad de asientos
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('semiautomatic', 'Semi-Automatic'),
        ('cvt', 'CVT')
    ]
    transmission = models.CharField(
        max_length=50,
        choices=TRANSMISSION_CHOICES,
        default='manual'
    )
    miles = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.make} {self.year}'