# Generated by Django 3.2.5 on 2021-08-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Обработано'),
        ),
    ]
