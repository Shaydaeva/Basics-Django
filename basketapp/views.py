from django.shortcuts import HttpResponseRedirect, get_object_or_404

from mainapp.models import Product
from basketapp.models import Basket


def basket_add(request, id_product=None):
    product = get_object_or_404(Product, id=id_product)
    baskets = Basket.objects.filter(user=request.user, product=product)

    def basket_add_quantity():
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        return basket_add_quantity()

    else:
        basket = baskets.first()
        return basket_add_quantity()


def basket_remove(request, id=None):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
