from django.shortcuts import render

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    # {'href': 'cart', 'name': 'корзина', 'route': 'cart/'}, -- не работает
]


def index(request):
    title = 'Главная страница'

    context = {
        'title': title,
        'links_menu': links_menu
    }

    return render(request, 'index.html', context)
    # return render(request=request, template_name='index.html', context=context)


def about(request):
    title = 'О нас'
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'about.html', context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, 'contact.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, 'cart.html', context)
