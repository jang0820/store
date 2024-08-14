#參考https://github.com/PacktPublishing/Django-4-by-example

from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from shop.models import Product
from .cart import Cart
from .forms import CartForm

class CartPushView(LoginRequiredMixin, FormView):
    form_class = CartForm
    template_name = 'cart_detail.html'
    login_url = '/accounts/login/'
    success_url = '/cart/'
    def form_valid(self, form):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.kwargs['pid'])
        quantity = form.cleaned_data['num']
        cart.push(product, num=quantity)
        return redirect('cart:cart_detail')

class CartPopView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    success_url = '/cart/'
    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pid')
        cart = Cart(request)
        product = get_object_or_404(Product, id=pid)
        if str(product.id) in cart.cart:
            cart.pop(product)
        return redirect('cart:cart_detail')

class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'cart_detail.html'
    login_url = '/accounts/login/'
    success_url = '/cart/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        for item in cart:  #呼叫__iter__
            item['num_form'] = CartForm(initial={'num': item['num']})
        context['cart'] = cart
        return context