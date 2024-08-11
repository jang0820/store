from django.urls import path

from . import views
app_name = "cart"

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='cart_detail'),
    path('push/(?P<pid>\d+)/', views.CartPushView.as_view(), name='cart_push'),
    path('pop/(?P<pid>\d+)/', views.CartPopView.as_view(), name='cart_pop'),
]