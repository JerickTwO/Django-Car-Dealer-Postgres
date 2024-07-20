from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(f'{value} is not a valid year. Year cannot be in the future.')
    if value < 1900:
        raise ValidationError(f'{value} is not a valid year. Year is too far in the past.')

class Car(models.Model):
    make = models.CharField(max_length=100)  # Marca del coche
    year = models.IntegerField(default=timezone.now().year, validators=[validate_year])  # Año del coche
    image = models.ImageField(upload_to='car_images/')  # Imagen del coche
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Precio del coche
    seating_capacity = models.IntegerField(default=0)  # Capacidad de asientos
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('semiautomatic', 'Semi-Automatic'),  # Añadiendo una opción más, si necesario
        ('cvt', 'CVT')  # Añadiendo otra opción más, si necesario
    ]
    transmission = models.CharField(
        max_length=50,
        choices=TRANSMISSION_CHOICES,
        default='manual'  # Valor por defecto
    )  # Tipo de transmisión
    miles = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Millas recorridas
    rating = models.IntegerField(default=0, validators=[
        lambda x: 0 <= x <= 5  # Asegurarse de que la calificación está entre 0 y 5
    ])  # Calificación en estrellas

    def __str__(self):
        return f'{self.make} {self.year}'

    def clean(self):
        # Método personalizado para validar el modelo en su conjunto
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")
        if self.miles < 0:
            raise ValidationError("Miles cannot be negative.")
        if self.seating_capacity < 1:
            raise ValidationError("Seating capacity must be at least 1.")
