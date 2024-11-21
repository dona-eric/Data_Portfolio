from django.contrib import admin

from .models import Projects, Skills, Articles, About, ServiceRequest, Services
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Élements Important', {"fields": ["title", "description", "skills_used", 'image_project']}),
        ('Information utiles', {"fields":["github_link", "url_project"]}),
        ]

admin.site.register(Projects, ProjectAdmin)
    
#admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Articles)
admin.site.register(About)
admin.site.register(ServiceRequest)
admin.site.register(Services)