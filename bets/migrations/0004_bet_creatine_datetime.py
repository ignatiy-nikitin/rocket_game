# Generated by Django 3.2.7 on 2021-10-04 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0003_auto_20211002_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='creatine_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата и время создания'),
            preserve_default=False,
        ),
    ]
