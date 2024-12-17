from django.forms import ModelForm
from .models import Contact, Service, Skill, ServiceRequest, Newsletter
from django import forms

class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields= ['name', "email", "subject_message", "content_message"]
    widgets = {
        'name' :forms.TextInput(attrs={"class": "form-control"}),
        'email' : forms.EmailInput(attrs={'class': "form-control"}),
        "subject_message": forms.TextInput(attrs={'class':"form-control"}),
        'content_message' : forms.TextInput(attrs={"class": "form-control"})
    }


class ServicesForms(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'icon', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du service', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description du service', 'class': 'form-control'}),
            'icon': forms.TextInput(attrs={'placeholder': 'Icône (ex. fa-solid fa-code)', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Prix', 'class': 'form-control'}),
        }
        exclude = ('icon', "price")


class ServiceRequestForms(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name_client', "email_client", "message"]

    widgets = {
        'name_client': forms.TextInput(attrs={"placeholder": 'Nom client', "class": 'form-control'}),
        'email_client': forms.EmailInput(attrs={"placeholder": 'Email client', "class": 'form-control'}),
        'message': forms.Textarea(attrs={"placeholder": 'Message', "class": 'form-control'})
    }

class NewsletterForms(forms.ModelForm):
    class Meta:
        model  = Newsletter
        fields = ['nom', 'prenom', "email"]

    widgets = {
        'nom': forms.TextInput(attrs={'placeholder': "Nom", "class": "form-control"}),
        'prenom': forms.TextInput(attrs={'placeholder': "prenom", "class": "form-control"}),
        'email': forms.EmailInput(attrs={'placeholder': "Email", "class": "form-control"})
    }


