from django.db import models
from merchants.models import Merchant

from providers.models import Provider

# Create your models here.
class Player(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='players', verbose_name='мерчант')
    id_ms = models.PositiveIntegerField(verbose_name='id в системе мерчанта')
    # public_token = models.CharField(max_length=256, verbose_name='публичный токен')
    private_token = models.CharField(max_length=256, verbose_name='публичный токен')

    # token = models.CharField(max_length=256, verbose_name='токен')
    # provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='users', verbose_name='провайдер')
    # balance = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='баланс')  # синхронизация с балансом провайдера?
    # active_bets = models.PositiveIntegerField(default=0, verbose_name='количество активных ставок')

    def __str__(self) -> str:
        return f'ID в системе партнера: {self.id_ms}'

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'