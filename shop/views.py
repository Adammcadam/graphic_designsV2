from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ A view to show all products """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shop/shop.html', context)

# def product(request):
#     """ A view to show singular products """
#     return render(request, 'shop/product.html', context)
