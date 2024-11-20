from django.contrib import admin

from .models import Projects, Skills, Articles, About, ServiceRequest, Services
# Register your models here.

admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Articles)
admin.site.register(About)
admin.site.register(ServiceRequest)
admin.site.register(Services)