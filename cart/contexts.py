from django.shortcuts import get_object_or_404
from shop.models import Product

# make this available to entire application
def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # iterate through each item in the cart 
    for item_id, item_data in cart.items():
        # check that there are no sizes 
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size,  quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': size
                })

    context = {
        'cart_items' : cart_items,
        'total' : total,
        'product_count' : product_count,
    }
    
    return context