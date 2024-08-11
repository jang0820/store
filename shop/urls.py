from django.urls import path

from . import views
app_name = "shop"
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_all'),
    path('(?P<slug>[-\w]+)/', views.ProductListView.as_view(), name='product_list_cat'),
    path('<int:id>/(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='product_detail'),
    ]