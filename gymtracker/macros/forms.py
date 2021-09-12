from .models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['nutritional_values_weight'].label = "Nutritional values per"
