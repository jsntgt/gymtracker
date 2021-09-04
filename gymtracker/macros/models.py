from django.db import models

UNIT_CHOICES = (
    ("gram", "g"),
    ("milliliter", "ml")
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    weight_unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default="gram")
    energy = models.DecimalField()
    fats = models.DecimalField()
    carbohydrates = models.DecimalField()
    proteins = models.DecimalField()
