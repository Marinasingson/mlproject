from django import forms

class DigitForm(forms.Form):
    image = forms.ImageField()
