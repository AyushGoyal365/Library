# Generated by Django 4.1.6 on 2024-01-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
