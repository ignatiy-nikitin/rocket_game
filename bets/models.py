from django.db import models

from players.models import Player


class Bet(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', 'Активная ставка'
        WIN = 'win', 'Выигрышная ставка'
        LOOSE = 'lose', 'Проигрышная ставка'
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='bets', verbose_name='игрок')
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='размер ставки')
    factor = models.PositiveIntegerField(verbose_name='множитель')
    status = models.CharField(max_length=32, choices=StatusChoices.choices, default=StatusChoices.ACTIVE,
                              verbose_name='статус')
