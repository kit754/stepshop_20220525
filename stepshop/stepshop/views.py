from django.shortcuts import render

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
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
