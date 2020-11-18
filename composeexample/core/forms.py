from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )

class GenerateRandomNameForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(50)
        ]
    )

class GenerateRandomNumberForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )