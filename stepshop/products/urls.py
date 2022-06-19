from django.urls import path
from products.views import products, product

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('product/<int:pk>/', product, name='product'),
]