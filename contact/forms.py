from django import forms

class contactForm(forms.Form):
    Ime=forms.CharField(required=True, max_length=100)
    Email=forms.EmailField(required=True)
    Komentar=forms.CharField(required=True,widget=forms.Textarea)
