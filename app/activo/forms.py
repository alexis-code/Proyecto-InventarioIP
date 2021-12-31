from django import forms
from django.db import models
from django.forms import fields

from .models import Activo

class ActivoForms(forms.ModelForm):
    class Meta:
        model = Activo
        fields = '__all__'
        