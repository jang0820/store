from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import  Http404
from django.views.generic.edit import FormView
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart
from accounts.views import debit, get_user_money, is_enough
from django.http import HttpResponseForbidden
from accounts.models import MyUser

class CheckoutView(FormView):
    template_name = 'checkout.html'
    form_class = OrderForm
    
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        tprice = cart.get_tprice()  #購物車總金額
        money = get_user_money(request.user) #儲值金
        self.initial = {"email":request.user.email, "address":request.user.address }
        if tprice > money: #儲值金不夠
            return HttpResponseForbidden("請先儲值，購買金額為"+str(tprice)+"儲值金為"+str(money)+"，儲值金不足無法購買") 
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        cart = Cart(self.request)
        debit(self.request.user, cart.get_tprice())   #從儲值金內扣款
        order = form.save(commit=False)
        order.user = self.request.user
        order.paid = True
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
        user = MyUser.objects.get(username = self.request.user)
        context['user'] = user
        return context
    
    @method_decorator(login_required)  #需要登入才能使用，修飾dispatch
    def dispatch(self, request, *arg, **kwargs):
        if (request.user.has_perm('order.order_create')): #需要權限order.order_create
            return super().dispatch(request, *arg, **kwargs)
        else:
            raise Http404()