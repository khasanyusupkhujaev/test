# Generated by Django 3.2 on 2021-06-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='post',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
