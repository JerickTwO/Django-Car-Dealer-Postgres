from django import forms
from django.utils import timezone
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'year', 'image', 'price', 'seating_capacity', 'transmission', 'miles', 'rating']
        widgets = {
            'year': forms.NumberInput(attrs={'min': 1900, 'max': timezone.now().year}),
            'price': forms.NumberInput(attrs={'step': 0.01}),
            'seating_capacity': forms.NumberInput(attrs={'min': 1}),
            'miles': forms.NumberInput(attrs={'step': 1}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5}),
        }

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        miles = cleaned_data.get('miles')
        seating_capacity = cleaned_data.get('seating_capacity')

        if price is not None and price < 0:
            self.add_error('price', "Price cannot be negative.")

        if miles is not None and miles < 0:
            self.add_error('miles', "Miles cannot be negative.")

        if seating_capacity is not None and seating_capacity < 1:
            self.add_error('seating_capacity', "Seating capacity must be at least 1.")

        return cleaned_data
