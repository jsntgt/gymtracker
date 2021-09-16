from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from .forms import ProductForm
from .models import Product
from django.template.loader import render_to_string
from django.http import JsonResponse


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

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            name = self.request.GET.get('name', None)
            products = Product.objects.filter(name__icontains=name)
            html = render_to_string(
                template_name="products_ajax.html",
                context={"products": products}
            )
            data_dict = {"html": html}
            return JsonResponse(data=data_dict, safe=False)
        context = {
            "object_list": self.get_queryset()
        }
        return render(request, self.template_name, context)

    def get_queryset(self):
        name = self.request.GET.get('name', None)
        if name is not None:
            return Product.objects.filter(name=name).order_by("name")
        else:
            return Product.objects.order_by("name")
