# Generated by Django 3.2.7 on 2021-09-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('weight_unit', models.CharField(choices=[('gram', 'g'), ('milliliter', 'ml')], default='gram', max_length=10)),
                ('energy', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fats', models.DecimalField(decimal_places=1, max_digits=10)),
                ('carbohydrates', models.DecimalField(decimal_places=1, max_digits=10)),
                ('proteins', models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
    ]