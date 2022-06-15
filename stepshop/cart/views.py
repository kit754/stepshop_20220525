from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect

from cart.models import Cart
from products.models import Product


def cart(request):
    if request.user.is_authenticated:
        cart_ = Cart.objects.filter(user=request.user)
        context = {
            'cart': cart_,
        }

        return render(request, 'cart/cart.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart_ = Cart.objects.filter(user=request.user, product=product).first()

    if not cart_:
        cart_ = Cart(user=request.user, product=product)

    cart_.quantity += 1
    cart_.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, pk):
    cart_record = get_object_or_404(Cart, pk=pk)
    cart_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

