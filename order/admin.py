from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_display = ['product', 'num', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'address', 'paid', 'createtime']
    list_filter = ['paid', 'createtime']
    inlines = [OrderItemInline]
