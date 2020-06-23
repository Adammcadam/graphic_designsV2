from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from shop.models import Product

# Create your views here.
def view_cart(request):
    """ A view to return the shopping cart """

    return render(request, 'cart/shopping-cart.html')

def add_to_cart(request, item_id):
    """ A view to add a product to the shopping cart """
    product = get_object_or_404(Product, pk=item_id)
    # convert to a integer 
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    cart = request.session.get('cart', {})

    if size:
        # check if item is in the bag 
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                # if item of that size in the bag increment the quantity 
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated {product.name} quantity to {cart[item_id]["items_by_size"][size]}!')
            else:
                # new size for that item 
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'{product.name} has been added to your cart!')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'{product.name} has been added to your cart!')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}!')
        else:
            cart[item_id] = quantity
            messages.success(request, f'{product.name} has been added to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    """ A view to update items in the shopping cart """
    product = get_object_or_404(Product, pk=item_id)
    # convert to a integer 
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    cart = request.session.get('cart', {})

    # if the item in the cart has a size update it
    if size:
        if quantity > 0: 
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]["items_by_size"][size]}!')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'{product.name} has been removed to your cart!')
    else:
        if quantity > 0: 
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}!')
        else:
            cart.pop(item_id)
            messages.success(request, f'{product.name} has been removed from your cart!')

    request.session['cart'] = cart
    return redirect(reverse('cart'))

def remove_from_cart(request, item_id):
    """ A view to remove items from the shopping cart """
    product = get_object_or_404(Product, pk=item_id)
    try:
        size = None
        if 'size' in request.POST:
            size = request.POST['size']
        cart = request.session.get('cart', {})

        # if the item in the cart has a size remove only that size
        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'{product.name} has been removed to your cart!')
        else:
            cart.pop(item_id)
            messages.success(request, f'{product.name} has been removed from your cart!')

        request.session['cart'] = cart
        # return a success response
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

