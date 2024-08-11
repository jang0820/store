#參考https://github.com/PacktPublishing/Django-4-by-example

from decimal import Decimal
from shop.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session #修改self.session就會修改request.session
        self.cart = self.session.get('CART', {})
        if not self.cart:
            self.session['CART'] = {}

    def push(self, product, num=1): #將product新增至購物車
        pid = str(product.id)
        if num <= 0 : return #數量不能小於等於0
        if pid not in self.cart:
            self.cart[pid] = {'num': 0, 'price': str(product.price)}        
        self.cart[pid]['num'] = num
        self.session['CART'] = self.cart
        self.session.modified = True  #資料儲存到session

    def pop(self, product): #購物車刪除商品product
        pid = str(product.id)
        if pid in self.cart:
            del self.cart[pid]
            self.session['CART'] = self.cart
            self.session.modified = True  #資料儲存到session

    def clear(self): #刪除session內的購物車資訊
        self.session.pop('CART', None)
        self.session.modified = True

    def __iter__(self): #for item in cart時，呼叫__iter__
        pids = self.cart.keys()
        prods = Product.objects.filter(id__in=pids)
        prods_map = {str(prod.id): prod for prod in prods}

        for pid in pids:
            prod = prods_map.get(pid)
            if prod:
                item = self.cart[pid]
                item['product'] = prod
                item['price'] = Decimal(item['price'])
                item['tprice'] = item['price'] * item['num']
                yield item

    def __len__(self):  #執行cart|length時，呼叫__len__
        return sum(item['num'] for item in self.cart.values())

    def get_tprice(self):
        return sum(Decimal(item['tprice']) for item in self.cart.values())