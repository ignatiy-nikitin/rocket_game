from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=256, verbose_name='название')
