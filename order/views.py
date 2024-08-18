from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import  Http404
from django.views.generic.edit import FormView
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart

class CheckoutView(FormView):
    template_name = 'checkout.html'
    form_class = OrderForm

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()

        for item in cart: # 創建 OrderItem來記錄購物車中的每一個項目
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                num=item['num']
            )
     
        cart.clear()  # 清空購物車
        return render(self.request, 'thank.html', {'order': order})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)  # 將購物車添加到context
        return context
    
    @method_decorator(login_required)  #需要登入才能使用，修飾dispatch
    def dispatch(self, request, *arg, **kwargs):
        if (request.user.has_perm('order.order_create')): #需要權限order.order_create
            return super().dispatch(request, *arg, **kwargs)
        else:
            raise Http404()