# Generated by Django 5.0.1 on 2024-01-17 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='email',
        ),
    ]