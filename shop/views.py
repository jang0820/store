#參考https://github.com/PacktPublishing/Django-4-by-example

from django.shortcuts import get_object_or_404

from cart.forms import CartForm
from .models import Category, Product
from django.views.generic import ListView, DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'list.html'  # 樣板路徑
    def get_context_data(self, **kwargs):
        cat = None
        cats = Category.objects.all()
        products = Product.objects.filter(available=True)
        if self.kwargs.get('slug'):
            slug = self.kwargs.get('slug')
            cat = get_object_or_404(Category, slug=slug)
            products = products.filter(category=cat)
        context = super().get_context_data(**kwargs)
        context["cat"] = cat
        context["cats"] = cats
        context["products"] = products
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop_detail.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('id')
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        context = super().get_context_data(**kwargs)
        context["product"] = product
        cartform = CartForm()
        context["cartform"] = cartform
        return context