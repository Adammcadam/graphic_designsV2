from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomQuoteForm

def custom_quote(request):
    """ A view to return the custom quote page """
    total_price = 0
    if request.method == 'POST':
        form = CustomQuoteForm(request.POST, request.FILES)
        if form.is_valid():
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
    }
    return render(request, template, context)
