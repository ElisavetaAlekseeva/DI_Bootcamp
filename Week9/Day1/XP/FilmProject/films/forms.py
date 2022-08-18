from dataclasses import fields
from datetime import datetime
from tkinter.ttk import Widget
from django import forms
from .models import (Director, Film, Review)
from datetime import date

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {'release_date': forms.DateInput(attrs={'type': 'date'}),
                    'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title of film'}),
                    # 'created_in_country': forms.SelectMultiple(attrs={'class': 'form-control'}),
                    # 'available_in_countries': forms.SelectMultiple(attrs={'class': 'form-control'}),
                    # 'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
                    'directors': forms.SelectMultiple(attrs={'class': 'form-control'}),
                    'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a link to image of film'}),
                }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        widgets = {
                    'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a first name'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a last name'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        