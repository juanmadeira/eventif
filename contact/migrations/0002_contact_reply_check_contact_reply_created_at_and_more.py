# Generated by Django 5.1 on 2024-12-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='reply_check',
            field=models.BooleanField(default=False, verbose_name='respondida'),
        ),
        migrations.AddField(
            model_name='contact',
            name='reply_created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='respondida em'),
        ),
        migrations.AddField(
            model_name='contact',
            name='response',
            field=models.TextField(blank=True, default='', max_length=200, verbose_name='resposta'),
        ),
    ]
