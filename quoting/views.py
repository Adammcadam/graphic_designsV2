from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomQuoteForm

def custom_quote(request):
    """ A view to return the custom quote page """
    total_price = 0
    if request.method == 'POST':
        form = CustomQuoteForm(request.POST, request.FILES)
        if form.is_valid():
            custom_product = form
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            total_price = ((length * width * height)/5000)
            custom_product.price = total_price
            print(total_price)
            form.save()
            messages.success(request, 'Successfully sent form. We have recieved your request and will in touch in due course')
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong please check the form for errors')
    else:
        form = CustomQuoteForm()

    template = 'quoting/quoting.html'
    context = {
        'form': form,
        'total_price': total_price
    }
    return render(request, template, context)
