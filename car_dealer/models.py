from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(f'{value} is not a valid year. Year cannot be in the future.')
    if value < 1900:
        raise ValidationError(f'{value} is not a valid year. Year is too far in the past.')


def validate_rating(value):
    if not (0 <= value <= 5):
        raise ValidationError("Rating must be between 0 and 5.")

class Car(models.Model):
    make = models.CharField(max_length=100)
    year = models.IntegerField(default=timezone.now().year, validators=[validate_year])
    image = models.ImageField(upload_to='car_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    seating_capacity = models.IntegerField(default=0)
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
    rating = models.IntegerField(default=0, validators=[validate_rating])

    def __str__(self):
        return f'{self.make} {self.year}'

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")
        if self.miles < 0:
            raise ValidationError("Miles cannot be negative.")
        if self.seating_capacity < 1:
            raise ValidationError("Seating capacity must be at least 1.")

