from django.db import models

from players.models import Player


class Deposit(models.Model):
    amount = models.IntegerField(verbose_name='размер депозита')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='deposits', verbose_name='игрок')
    currency = models.CharField(max_length=256)
    creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')