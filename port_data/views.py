from django.shortcuts import render, redirect, get_object_or_404
from .models import About, Articles, Projects, Skills, Contacts, Services, ServiceRequest
from .forms import ContactForms, ServicesForms, ServiceRequestForms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Page d'accueil

@login_required
def home(request):
    return render(request, 'portfolio/home.html')


# Page "À propos de moi"
def about(request):
    about_me = About.objects.first() 
    return render(request, 'portfolio/about.html', {'about': about_me})


# Page des articles de blog
def articles(request):
    blog_article = Articles.objects.all()
    return render(request, 'portfolio/blog.html', {'blog_article': blog_article})

#pour une article spécifique

def article_list(request, id_article):
    blog_list = Articles.objects.get(id_article = id_article)
    if blog_list:
        return render(request, 'portfolio/blog_list.html',
        {'blog_list': blog_list})
    else:
        return render(request, 'portfolio/blog.html', {'blog_article': blog_article})


# Page des compétences
def skills(request):
    skill = Skills.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skill})


# Page des projets
def projects(request):
    project = Projects.objects.all()  
    return render(request, 'portfolio/projects.html', {'project': project})


# Page des contacts
def contacts(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject_message = form.cleaned_data['subject_message']
            content_message = form.cleaned_data['content_message']
             # Assemblage du message
            full_message = f"Message de {name} ({email}):\n\n{content_message}"

            # Envoi de l'email
            send_mail(
                subject=f"Message from {name} via Contact Us: {subject_message}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_TO_EMAIL],
                fail_silently=False,
            )
        return redirect ('contacts-us')
    else:
        form = ContactForms()
    return render(request, 'portfolio/contacts.html', 
                  {'form': form})


# page des services

def services(request):
    service =  Services.objects.all()
    return render(request, 'portfolio/services.html',
                  {'service_list': service})



def services_request(request):
    service = get_object_or_404(Services)  # Trouve un service, vous pouvez aussi ajouter un paramètre d'ID si nécessaire
    if request.method == 'POST':
        form = ServiceRequestForms(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service = service  # Associe le service au formulaire
            service_request.save()
            return redirect('services')  # Redirige après avoir sauvegardé la demande
    else:
        form = ServiceRequestForms()
    
    return render(request, 'portfolio/services_request.html', {'service': service, 'form': form})
