from django.forms import ModelForm
from . models import Photo
from django import forms
from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo

        fields = ['title', "image"]