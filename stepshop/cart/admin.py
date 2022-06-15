from django.contrib import admin

from cart.models import Cart

admin.site.register(Cart)  # создается пункт меню в админке
