from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from .forms import ProductForm
from .models import Product


class ProductFormView(CreateView):
    template_name = "product_form.html"
    form_class = ProductForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    template_name = "product_detail.html"

    def get_object(self, queryset=None):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

    def get_queryset(self):
        return Product.objects.order_by("name")
