from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from .models import About, Article, Project, Skill, Contact, Service, ServiceRequest, Newsletter
from .forms import ContactForms, ServicesForms, ServiceRequestForms, NewsletterForms
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.urls import reverse
from django.views.generic.edit import FormView
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
# Page d'accueil

#login_required

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'


# Page "À propos de moi"


class AboutView(DetailView):
    model = About
    template_name = 'portfolio/about.html'

    def get_object(self):
        return About.objects.first()



# Page des articles dew blog
def article(request):
    blog_article = Article.objects.all().order_by('-date_published')
    print(blog_article)
    return render(request, 'portfolio/blog.html', {'blog_article': blog_article})

#pour une article spécifique

def article_list(request, id_article):
    try:
        blog_list = Article.objects.get(pk=id_article) 
        return render(request, 'portfolio/blog_list.html', {'blog_list': blog_list})
    except Exception as e:
        return render(request, 'portfolio/blog.html', {'blog_article': blog_list})


# Page des compétences
def skills(request):
    skill = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skill})


# Page des projets
def projects(request):
    project = Project.objects.all()  
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
            try:
                send_mail(
                    subject=f"Message from {name} via Contact Us: {email}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list= settings.EMAIL_LIST,
                    fail_silently=False,
                )
                return HttpResponse('Email envoyé avec suucès !')
            except Exception as e:
                return HttpResponse(f"Erreur lors de l'email, veuillez ressayez; {e}")
    else:
        form = ContactForms()
    return render(request, 'portfolio/contacts.html', 
                  {'form': form})


# page des services

def services(request):
    service =  Service.objects.all()
    return render(request, 'portfolio/services.html',
                  {'service_list': service})

def services_detail(request, id_service):
    try:
        service_detail = Service.objects.get(pk= id_service)
        return render(request, 'portfolio/service_detail.html', {'service_detail': service_detail})
    except Exception as e:
        return HttpResponse(f"Erreur survenue {str(e)}")




def services_request(request, id_service=None):  # Paramètre service_id ajouté
    # Récupérer le service spécifique ou retourner 404 si non trouvé
    service = get_object_or_404(Service, pk=id_service) if id_service else None
    
    if request.method == 'POST':
        form = ServiceRequestForms(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            if service:
                service_request.service = service
            service_request.save()
            messages.success(request, 'Votre demande de service a été envoyée avec succès!')
            return redirect('services')
    else:
        form = ServiceRequestForms()
        if service:
            form.initial = {'service': service}
    
    contexte = {
        'form': form,
        'service': service,
    }
    return render(request, 'portfolio/services_request.html', contexte)



"""vue pour les newsletters """

def newsletters(request):
    if request.method == 'POST':
        form = NewsletterForms(request.POST)
        if form.is_valid():
            try:
                nom = form.cleaned_data['nom']
                email = form.cleaned_data['email']
                validate_email(email)

                # verifier si le mail existe déja
                news, created = Newsletter.objects.get_or_create(email = email,
                                                                 defaults={"nom": nom})
                if created:

                    admin_message = f"""
                                Nouvelle Inscription à la newsletter !
                                Details de l'inscription :
                                -Nom :{nom}
                                -Email: {email}
                                Pour tous les details , connectez-vous au site de l'administrateur
                                """
                    send_mail(
                        subject= 'Nouvelle inscription à la Newsletter',
                        message= admin_message,
                        from_email= settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.ADMIN_EMAIL],
                        fail_silently= False,
                    )
                    messages.success(request, f'Merci {nom} ! Vous etes inscrit à la newsletter')
                else:
                    messages.info(
                        request, "Cette adresse est déja inscrite à notre newsletter"
                    )
                return redirect('home')
            except ValidationError:
                messages.error(
                    request, "Veuillez fournir une adresse email valide"
                )
            except Exception as e:
                messages.error(request, "Une erreur est survenue lors de l'inscription. Veuillez réessayer")
    else:
        form = NewsletterForms()
    return render(request, 'portfolio/newsletters.html', 
                  {'form': form,
                   'title': 'Inscription à la newsletter',
                   "description": "Restez informé de nos dernières actualités"})



            

""" Une fonction qui valide tout les formulaires de la base avec get ou post"""

class FormValidationMixin:

    ## mixin pour la validation des formulaires avec gestion des messages
    def form_valid(self, form):
        try:
            self.object = form.save()
            messages.success(self.request, self.get_success_message())
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            messages.error(
                self.request,
                f"Une erreur est survenue: {str(e)}"
            )
            return self.form_invalid(form)
        

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Veuillez corriger les erreurs dans le formulaire"
        )
        return super().form_invalid(form)
    
    def get_success_message(self):
        return f"Vos modifications ont été prises en compte !"

    def get_success_url(self):
        return reverse('home')






