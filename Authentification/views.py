from django.shortcuts import render, redirect
from . forms import LoginForm, InscriptionForm, AssistantForm
from django.contrib.auth import login, logout, authenticate
from . models import User
from django.views.generic import View
from . import forms
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from Authentification.chatbot import get_response
from django.http import JsonResponse
from django.contrib import messages


# vue pour la connexion utilisateur

def home(request):
    return render(request, 'portfolio/home.html')

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
                return redirect('home')
        else:
            message = f"Identifiant invalides"

        return render(request, 'authenticate/login.html',
                  context={"form": form, "message": message
                           })


# deconnexion des utilisateurs

def logout_user(request):
    messages.success(request, "Logout Successfully !")
    return redirect('home')



# vue basée sur l'inscrption

def Inscription(request):
    #form  = InscriptionForm()
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = InscriptionForm()       
    return render(request, 'authenticate/register.html', context={'form': form})


# vue du chatbot

def chatbot_view(request):
    response_user = None
    if request.method =='POST':
        form = AssistantForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message'] # recuperer les questions
            response_user = get_response(user_message)
            print('Message Utilisateur:', user_message)
            print("Reponse:", response_user)
        else:
            print('Désolé, Je ne comprends pas votre question')
    else:
        form = AssistantForm()
    return render(request, 'authenticate/chatbot.html',
                  context={'form': form, 'response_user': response_user})


