from django.urls import path

from cart.views import cart, cart_add, cart_remove

app_name = 'cart'

urlpatterns = [
    path('', cart, name='view'),
    path('add/<int:pk>/', cart_add, name='add'),
    path('remove/<int:pk>/', cart_remove, name='remove'),
]
