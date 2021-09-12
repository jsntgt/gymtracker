from django.db import models
from django.urls import reverse

UNIT_CHOICES = (
    ("gram", "g"),
    ("milliliter", "ml")
)
WEIGHT_VALUES_CHOICES = (
    ("100g", "100g"),
    ("100ml", "100ml"),
    ("serving", "serving")
)


class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    weight_unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default="gram")
    nutritional_values_weight = models.CharField(max_length=10, choices=WEIGHT_VALUES_CHOICES, default="100g")
    energy = models.DecimalField(max_digits=10, decimal_places=1)
    fats = models.DecimalField(max_digits=10, decimal_places=1)
    carbohydrates = models.DecimalField(max_digits=10, decimal_places=1)
    proteins = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(default='', upload_to='product_images')

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id": self.pk})
