from django import forms
from .models import Category_mod

class Category_form(forms.Form):
    name = forms.CharField()
    image = forms.URLField()


class ToDO_form(forms.Form):

    title = forms.CharField()
    details = forms.Textarea()
    deadline_date = forms.DateField()
    category = forms.ModelChoiceField(queryset=Category_mod.objects.all())
