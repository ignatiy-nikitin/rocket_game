from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=256, verbose_name='название')