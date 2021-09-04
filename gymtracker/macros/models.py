from django.db import models
from django.urls import reverse

UNIT_CHOICES = (
    ("gram", "g"),
    ("milliliter", "ml")
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    weight_unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default="gram")
    energy = models.DecimalField(max_digits=10, decimal_places=1)
    fats = models.DecimalField(max_digits=10, decimal_places=1)
    carbohydrates = models.DecimalField(max_digits=10, decimal_places=1)
    proteins = models.DecimalField(max_digits=10, decimal_places=1)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id": self.pk})
