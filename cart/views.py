from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """ A view to return the shopping cart """

    return render(request, 'cart/shopping-cart.html')

def add_to_cart(request, item_id):
    """ A view to add a product to the shopping cart """
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
            else:
                # new size for that item 
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    """ A view to update items in the shopping cart """
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
        else:
            del cart[item_id]['items_by_size'][size]
    else:
        if quantity > 0: 
            cart[item_id] = quantity
        else:
            del cart.pop[item_id]

    request.session['cart'] = cart
    return redirect(reverse('cart'))
