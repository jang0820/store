from django.db import models
from shop.models import Product
from accounts.models import MyUser

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, 
                             related_name='orders')
    email = models.EmailField()
    address = models.CharField(max_length=250)
    createtime = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-createtime']
        permissions = (
            ("order_delete", "Can Delete Order"),
            ("order_create", "Can Create Order"),
            ("order_update", "Can Update Order"),
        )

    def __str__(self):
        return f'Order {self.id} - {self.user}'

    def get_tcost(self):
        return sum(item.get_cost() for item in self.order_orderitems.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, 
                              related_name='order_orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                related_name='product_orderitems')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    num = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.num
