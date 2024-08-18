from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.conf.urls import  include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("cart/", include('cart.urls')),
    path("order/", include('order.urls')),
    path("", include('shop.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)