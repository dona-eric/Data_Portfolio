from django.forms import ModelForm
from .models import Contacts, Services, Skills, ServiceRequest
from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    subject_message = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    content_message = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))


class ServicesForms(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'description', 'icon', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du service', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description du service', 'class': 'form-control'}),
            'icon': forms.TextInput(attrs={'placeholder': 'Icône (ex. fa-solid fa-code)', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Prix', 'class': 'form-control'}),
        }


class ServiceRequestForms(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['client_name', "client_email", "message"]

    widgets = {
        'client_name': forms.TextInput(attrs={"placeholder": 'Nom client', "class": 'form-control'}),
        'client_email': forms.EmailInput(attrs={"placeholder": 'Email client', "class": 'form-control'}),
        'message': forms.Textarea(attrs={"placeholder": 'Message', "class": 'form-control'})
    }
