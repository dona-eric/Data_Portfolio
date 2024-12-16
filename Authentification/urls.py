from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views
import Authentification.views
urlpatterns = [
    path('home/register/', views.home, name = 'home'),
    path('register/', views.Inscription, name = 'register'),
    path('login/', Authentification.views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('portfolioia/', views.chatbot_view, name='portfolioia')
]