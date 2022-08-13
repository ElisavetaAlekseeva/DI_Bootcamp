from typing import ForwardRef
from unicodedata import name
from django import forms
from .models import Category_model, Gif_model


class Category_form(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)

class Gif_form(forms.Form):
    title = forms.CharField(min_length=3, max_length=100)
    url = forms.URLField()
    uploader_name = forms.CharField(min_length=3, max_length = 100)
    category = forms.ModelMultipleChoiceField(queryset= Category_model.objects.all())
