from django.shortcuts import get_object_or_404
from shop.models import Product

# make this available to entire application
def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # iterate through each item in the cart 
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_items' : cart_items,
        'total' : total,
        'product_count' : product_count,
    }
    
    return context