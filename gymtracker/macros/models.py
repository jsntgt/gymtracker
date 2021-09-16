from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

UNIT_CHOICES = (
    ("g", "g"),
    ("ml", "ml")
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
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id": self.pk})

    def __str__(self):
        return f'Product {self.name} added by {self.author}'
