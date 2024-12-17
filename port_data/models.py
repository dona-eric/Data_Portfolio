from django.db import models


""" Here we create other that the models of database of website
portfolio """

"""Models  for About"""

class About(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=150)
    biography = models.TextField()
    profil_pictures = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    resume_link = models.URLField(blank=True, null=True) # url vers mon cv

    def __str__(self):
        return self.nom
    
"""models for projects"""

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    skills_used = models.CharField(max_length=500) ## les compétences techniques utilisées
    image_project = models.ImageField(upload_to='portfolio_projects/',blank=True, null=True)
    github_link = models.URLField(blank=True, null=True) ## lien vers le repo github
    url_project = models.URLField(blank=True, null=True) ## lien vers un demo ou application deployée
    date_project_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.title} ({self.description})"


"""models for skills"""

class Skill(models.Model):
    category = models.CharField(max_length=200)
    skills_name = models.CharField(max_length=100)
    level = models.IntegerField(default=50)
    description = models.TextField(null=True)
    def __str__(self):
        return f" {self.skills_name} ({self.category})"



"""models for articles """

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    #image_blog = models.ImageField(upload_to='portfolio_articles/', blank=True, null=True)
    url_blog = models.URLField(blank=True, null=True)
    author_articles = models.CharField(max_length=200, verbose_name='auteur', null=True)
    date_published = models.DateTimeField(auto_now_add=True,null=True, verbose_name='Date de publication')
    categorie = models.TextField(blank=True, null = True)
    def __str__(self):
        return self.title


"""models for contacts: i would like to use the forms of django 
to create it """

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique = True)
    subject_message = models.TextField()
    content_message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True, null=True)
    is_read = models.BooleanField(default=True)

    def __str__(self):
        content=f"Vous avez reçu un message de : {self.email}"
        return content

# mes services 
class Service(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    icon = models.TextField(null =True, blank=True)
    price = models.IntegerField(default=50)


## models pour permettre à un client de demander des services

class ServiceRequest(models.Model):
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name='request')
    name_client = models.CharField(max_length=150)
    email_client = models.EmailField(unique = True)
    message = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Demande de service de {self.name_client} ({self.email_client}) pour {self.service}"



## models pour la newsletter 
class Newsletter(models.Model):
    nom = models.CharField(max_length=100, verbose_name='name')
    prenom = models.CharField(max_length=200, verbose_name = 'surname')
    email = models.EmailField(unique=True, blank=True, null=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(auto_created=True)

    def __str__(self):
        return self.email