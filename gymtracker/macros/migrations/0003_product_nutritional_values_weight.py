# Generated by Django 3.2.7 on 2021-09-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macros', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutritional_values_weight',
            field=models.CharField(choices=[('100g', '100g'), ('serving', 'serving')], default='100g', max_length=10),
        ),
    ]