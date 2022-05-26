from django.urls import path
from products.views import products, product

urlpatterns = [
    path('', products),
    path('product/', product),
]