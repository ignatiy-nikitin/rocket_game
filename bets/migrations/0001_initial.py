# Generated by Django 3.2.7 on 2021-10-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='размер ставки')),
                ('factor', models.PositiveIntegerField(verbose_name='множитель')),
                ('status', models.CharField(choices=[('active', 'Активная ставка'), ('win', 'Выигрышная ставка'), ('loose', 'Проигрышная ставка')], default='active', max_length=32, verbose_name='статус')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
            ],
        ),
    ]
