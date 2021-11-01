from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=256, verbose_name='название')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'