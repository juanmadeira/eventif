# Generated by Django 5.1 on 2024-11-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=20, verbose_name='telefone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('paid', models.BooleanField(default=False, verbose_name='pago')),
            ],
            options={
                'verbose_name': 'inscrição',
                'verbose_name_plural': 'inscrições',
            },
        ),
    ]
