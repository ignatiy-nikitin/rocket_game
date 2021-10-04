from django.db import models

from providers.models import Provider

# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=256, verbose_name='никнейм')
    token = models.CharField(max_length=256, verbose_name='токен')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='users', verbose_name='провайдер')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='баланс')  # синхронизация с балансом провайдера?
    active_bets = models.PositiveIntegerField(default=0, verbose_name='количество активных ставок')
