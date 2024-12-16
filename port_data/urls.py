from django.urls import path, include

from . import views
from .views import HomeView, AboutView

urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('about-me/', AboutView.as_view(), name='about'),
    #path('skills/', views.skills, name = 'skills'),
    path('projects/', views.projects, name="projects"),
    path('contacts-us/', views.contacts, name="contacts-us"),
    path('services/', views.services, name ="services"),
    path('services_request/<int:id_service>/', views.services_request, name ="service_request_with_id"),
    path('services_request/', views.services_request, name = 'services_request'),
    path('blog/', views.article, name='blog'),
    path('news/', views.newsletters, name = 'news')

]
