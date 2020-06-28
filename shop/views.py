from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm

# Create your views here.
def all_products(request):
    """ A view to show all products """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shop/shop.html', context)

def product_page(request, product_id):
    """ A view to show singular products """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'shop/product.html', context)

@login_required
def add_product(request):
    """ A view for super users to add products """
    if not request.user.is_superuser:
        messages.error(request, 'Unfortunately only the super user can add/update/delete products')
        return redirect(reverse('home'))
        
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added a product')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Something went wrong, please check the form for errors')
    else: 
        form = ProductForm()
        template = 'shop/add_product.html'
        context = {
            'form': form,
        }
    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ A view for super users to edit products """
    if not request.user.is_superuser:
        messages.error(request, 'Unfortunately only the super user can add/update/delete products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product,  pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully updated {product.name}')
            return redirect(reverse('product_page', args=[product_id]))
        else:
            messages.error(request, 'Something went wrong, please check the form for errors')
    else:
        edit_form = ProductForm(instance=product)

    template = 'shop/edit_product.html'
    context = {
        'edit_form': edit_form,
        'product': product
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ A view for super users to delete products """
    if not request.user.is_superuser:
        messages.error(request, 'Unfortunately only the super user can add/update/delete products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product,  pk=product_id)
    product.delete()
    messages.success(request, 'The product has been deleted successfully')
    return redirect(reverse('product_page', args=[product_id]))
