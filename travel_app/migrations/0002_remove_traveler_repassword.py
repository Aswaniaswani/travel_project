# Generated by Django 4.1.7 on 2023-03-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveler',
            name='repassword',
        ),
    ]