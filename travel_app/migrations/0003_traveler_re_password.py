# Generated by Django 4.1.7 on 2023-03-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_remove_traveler_repassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='re_password',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
