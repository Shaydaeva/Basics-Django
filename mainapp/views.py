from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'product_categories': ProductCategory.objects.all(),
    }

    return render(request, 'mainapp/products.html', context)

