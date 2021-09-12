# Generated by Django 3.2.7 on 2021-09-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background',
            field=models.ImageField(default='default_background.png', upload_to='background_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile.jpg', upload_to='profile_pics'),
        ),
    ]
