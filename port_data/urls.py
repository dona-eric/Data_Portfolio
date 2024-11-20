from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('skills/', views.skills, name = 'skills'),
    path('projects/', views.projects, name="projects"),
    path('contacts-us/', views.contacts, name="contacts-us"),
    path('services/', views.services, name ="services"),
    path('services_request/', views.services_request, name = 'services_request'),
    path('blog/', views.articles, name='blog')

]
