# Generated by Django 3.2 on 2021-06-05 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='media',
            new_name='post',
        ),
    ]
