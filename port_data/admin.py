from django.contrib import admin

from .models import Project, Skill, Newsletter, Article, Contact, About, ServiceRequest, Service
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Élements Important', {"fields": ["title", "description", "skills_used", 'image_project']}),
        ('Information utiles', {"fields":["github_link", "url_project"]}),
        ]

admin.site.register(Project, ProjectAdmin)

admin.site.register(About)
admin.site.register(Service)


@admin.register(ServiceRequest)
class ServiceRequestdmin(admin.ModelAdmin):
    list_display = ("name_client","email_client", "message", "date_requested")
    list_filter =("name_client", "email_client", 'message')
    search_fields = ("name_client", "email_client")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_articles', 'date_published', 'categorie', 'content')
    list_filter = ('author_articles', 'categorie', 'date_published')
    search_fields = ('title', 'content', 'author_articles')
    date_hierarchy = 'date_published'
    ordering = ('-date_published',)
    

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'subscribed_at', 'is_active')
    list_filter = ('subscribed_at', "is_active")
    search_fields = ('email', 'nom')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category', 'skills_name', "level")
    search_fields = ('category', "level", "description")



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject_message', 'content_message', 'sent_at', 'is_read')
    list_filter = ('is_read', 'sent_at')
    search_fields = ('name', 'email', 'subject_message', 'content_message')

