from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart!")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51GrP31CknKlaY20INbzItLd2sD45cPrfYbpoFfsz9ixssEErWeLmF1e85y3iXyhBSZlcyQwPdMSpupGxgOUrhsGB00vwaskfno',
        'stripe_secret' : 'test'
    }

    return render(request, template, context)