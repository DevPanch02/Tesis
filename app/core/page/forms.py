from django import forms
from core.page.models import Page
from django.forms import ModelForm


class PageForm(ModelForm):
    class Meta:
        model=Page
        fields='image_page','description'

        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese descripcion'}),
        }