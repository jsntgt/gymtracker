# Generated by Django 3.2.7 on 2021-09-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('barbell', 'Barbell'), ('dumbbell', 'Dumbbell'), ('machine_other', 'Machine/Other'), ('weighted_bodyweight', 'Weighted Bodyweight'), ('assisted_bodyweight', 'Assisted Bodyweight'), ('reps_only', 'Reps only'), ('cardio', 'Cardio'), ('duration', 'Duration')], default='gram', max_length=20)),
            ],
        ),
    ]
