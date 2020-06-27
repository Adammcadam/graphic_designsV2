from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents
from .models import Order, OrderItem
from shop.models import Product
from profiles.models import UserProfile

import stripe

def checkout(request):
    """ 
    A view to display the checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name' : request.POST['full_name'],
            'email' : request.POST['email'],
            'phone_number' : request.POST['phone_number'],
            'address_line1' : request.POST['address_line1'],
            'address_line2' : request.POST['address_line2'],
            'city' : request.POST['city'],
            'postcode' : request.POST['postcode'],
            'country' : request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            # get the stripe pid and save it  to the order 
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                size=size,
                            )
                            order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found. ")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # User requested to save info 
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please check your form and try again')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is currently empty!")
            return redirect(reverse('shop'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        # make sure its in pence rather than pounds for stripe 
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        # Auto fill the delivery details if they have a user profile 
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name' : profile.user.get_full_name(),
                    'email' : profile.user.email,
                    'address_line1': profile.default_address_line1,
                    'address_line2': profile.default_address_line2,
                    'city': profile.default_city,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                    'phone_number': profile.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
        
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key' : stripe_public_key,
            'client_secret' : intent.client_secret
        }

    return render(request, template, context)

def checkout_success(request, order_number):
    """ 
    Success page for checkouts
    """
    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_address_line1': order.address_line1,
                'default_address_line2': order.address_line2,
                'default_city': order.city,
                'default_postcode': order.postcode,
                'default_country': order.country,
                'default_phone_number': order.phone_number,
            }
            user_profile_form =  UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed  \
            Your order number is {order_number}. Confirmation \
            will be sent to {order.email}.')
    # remove the users cart items from the session
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }

    return render(request, template, context)