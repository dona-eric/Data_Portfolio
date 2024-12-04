from django.db import models
from django.conf import settings

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length = 500)
    image = models.ImageField()
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created_at = models.DateTimeField(auto_now_add=True)



