from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CATEGORY_CHOICES = (
    ("barbell", "Barbell"),
    ("dumbbell", "Dumbbell"),
    ("machine_other", "Machine/Other"),
    ("weighted_bodyweight", "Weighted Bodyweight"),
    ("assisted_bodyweight", "Assisted Bodyweight"),
    ("reps_only", "Reps only"),
    ("cardio", "Cardio"),
    ("duration", "Duration"),
)
BODY_PART_CHOICES = (
    ("core", "Core"),
    ("arms", "Arms"),
    ("back", "Back"),
    ("chest", "Chest"),
    ("legs", "Legs"),
    ("shoulders", "Shoulders"),
    ("other", "Other"),
    ("olympic", "Olympic"),
    ("full_body", "Full Body"),
    ("cardio", "Cardio")
)


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='barbell')
    body_part = models.CharField(max_length=20, choices=BODY_PART_CHOICES, default='other')
    instructions = models.TextField(max_length=400, blank=True)
    photo = models.ImageField(upload_to='exercise_pics', blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"{self.author.username}'s-{self.name} template"


class Workout(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.template.user.username} workout from {self.date}"


class Set(models.Model):
    reps = models.IntegerField()
    weight = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
