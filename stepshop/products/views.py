from django.shortcuts import render, get_object_or_404

from products.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/category/0/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def products(request, pk=None):
    title = 'Продукты'

    products_ = Product.objects.all()
    # products_ = Product.objects.all().filter(category__name__in=['Джинсы', 'Кеды']).order_by('price')
    # products_ = Product.objects.all().filter(category__name='Джинсы', price__lt=600) - фильтр по имени товара
    # products_ = Product.objects.all().filter(category__name__endswith='ы') - товар кончается на "ы"
    # products_ = Product.objects.all().exclude(category__name__startswith='Д') - исключи
    # products_ = Product.objects.all().get(startswith='Д')
    categories = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products_,
            'categories': categories,
            'category': category,
        }
        return render(request, 'products.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
    }

    return render(request, 'products.html', context)


def product(request):
    return render(request, 'product.html')
