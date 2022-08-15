from datetime import datetime
from tkinter.ttk import Widget
from django import forms
from .models import (Director, Film)
from datetime import date

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {'release_date': forms.DateInput(attrs={'type': 'date'})}

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
