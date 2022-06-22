from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse

from cart.models import Cart
from products.models import Product

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


@login_required
def cart(request):
    if request.user.is_authenticated:
        cart_ = Cart.objects.filter(user=request.user)
        context = {
            'cart': cart_,
            'links_menu': links_menu,
        }

        return render(request, 'cart/cart.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)

    cart_ = Cart.objects.filter(user=request.user, product=product).first()

    if not cart_:
        cart_ = Cart(user=request.user, product=product)

    cart_.quantity += 1
    cart_.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_remove(request, pk):
    cart_record = get_object_or_404(Cart, pk=pk)
    cart_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

