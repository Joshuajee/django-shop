# Generated by Django 4.2.7 on 2024-01-18 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
    ]
