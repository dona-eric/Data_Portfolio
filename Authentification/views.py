from django.shortcuts import render, redirect
from . forms import LoginForm, InscriptionForm
from django.contrib.auth import login, logout, authenticate
from . models import User
from django.views.generic import View
from . import forms
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

# vue pour la connexion utilisateur

class LoginView(View):
    template_name = 'authenticate/login.html'
    form_class = LoginForm

    def get(self, request):
        form= self.form_class()

        message = ""
        return render(request, self.template_name, context={'form': form, "message": message})

    def post(self, request):
        message = ""
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email']
            )
            if user is not None:
                login(request, user)
                message = f"Bonjour ! {user.username}, vous etes connectés !"
                return redirect ('home')
            else:
                message = f"Identifiant invalides"

        return render(request, 'authenticate/login.html',
                  context={"form": form, "message": message
                           })


# deconnexion des utilisateurs

def logout_user(request):
    logout(request)
    return redirect('home')



# vue basée sur l'inscrption

def Inscription(request):
    form  = InscriptionForm()
    if request.method == 'POST':
        InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        
    return render(request, 'authenticate/register.html',
                  context={'form': form})