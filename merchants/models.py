from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser


class Merchant(AbstractUser):
    name = models.CharField(max_length=256, verbose_name='название')
    # username = models.CharField(max_length=256, verbose_name='login для входа')
    # password = models.CharField(max_length=256, verbose_name='пароль')
    # auth_token = models.CharField(max_length=256, verbose_name='auth токен')
    # creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')

    first_name = None
    last_name = None

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'