from django import forms

from products.models import Proizvod

class ProizvodForm(forms.ModelForm):
    class Meta:
        model=Proizvod
        fields=[
            'kategorija',
            'materijal',
            'image',
        ]

