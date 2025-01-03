from django import forms
from .models import Jewelry

class JewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = ['name', 'description', 'initial_price', 'image_1', 'image_2', 'image_3']

    def clean_initial_price(self):
        initial_price = self.cleaned_data.get('initial_price')
        if initial_price is not None and initial_price < 0:
            raise forms.ValidationError("Initial price must be greater than zero.")
        return initial_price