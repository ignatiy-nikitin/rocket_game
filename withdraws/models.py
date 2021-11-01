from django.db import models

from players.models import Player


class Withdraw(models.Model):
    amount = models.IntegerField(verbose_name='размер снятия')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='withdraws', verbose_name='игрок')
    currency = models.CharField(max_length=256)
    creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')

    class Meta:
        verbose_name = 'Снятие'
        verbose_name_plural = 'Снятия'