# Generated by Django 3.2 on 2021-06-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_photos_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='post',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic/'),
        ),
    ]
