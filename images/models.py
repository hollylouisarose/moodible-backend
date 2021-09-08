from django.db import models

# Create your models here.
class Image(models.Model):
    source = models.CharField(max_length=200)
    description = models.CharField(max_length=100)