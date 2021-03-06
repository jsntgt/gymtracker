# Generated by Django 3.2.7 on 2021-09-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='body_part',
            field=models.CharField(choices=[('core', 'Core'), ('arms', 'Arms'), ('back', 'Back'), ('chest', 'Chest'), ('legs', 'Legs'), ('shoulders', 'Shoulders'), ('other', 'Other'), ('olympic', 'Olympic'), ('full_body', 'Full Body'), ('cardio', 'Cardio')], default='other', max_length=20),
        ),
        migrations.AddField(
            model_name='exercise',
            name='instructions',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='exercise',
            name='photo',
            field=models.ImageField(blank=True, upload_to='exercise_pics'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.CharField(choices=[('barbell', 'Barbell'), ('dumbbell', 'Dumbbell'), ('machine_other', 'Machine/Other'), ('weighted_bodyweight', 'Weighted Bodyweight'), ('assisted_bodyweight', 'Assisted Bodyweight'), ('reps_only', 'Reps only'), ('cardio', 'Cardio'), ('duration', 'Duration')], default='reps_only', max_length=20),
        ),
    ]
