#參考https://github.com/PacktPublishing/Django-4-by-example

from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views import View

from shop.models import Product
from .cart import Cart
from .forms import CartForm

class CartPushView(FormView):
    form_class = CartForm
    template_name = 'cart_detail.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.kwargs['pid'])
        quantity = form.cleaned_data['num']
        cart.push(product, num=quantity)
        return redirect('cart:cart_detail')

class CartPopView(View):

    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pid')
        cart = Cart(request)
        product = get_object_or_404(Product, id=pid)
        if str(product.id) in cart.cart:
            cart.pop(product)
        return redirect('cart:cart_detail')

class CartDetailView(TemplateView):
    template_name = 'cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        for item in cart:  #呼叫__iter__
            item['num_form'] = CartForm(initial={'num': item['num']})
        context['cart'] = cart
        return context