# Generated by Django 3.2.7 on 2021-09-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='product_images'),
        ),
    ]