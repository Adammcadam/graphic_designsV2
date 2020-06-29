from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from .forms import CustomQuoteForm

def custom_quote(request):
    """ A view to return the custom quote page """
    if request.method == 'POST':
        custom_form = CustomQuoteForm(request.POST, request.FILES)
        if custom_form.is_valid():
            custom_quote = custom_form.save()

            # send custom request to client and user
            customer_email = custom_quote.email
            customer_subject = render_to_string(
                'quoting/confirmation_emails/customer_confirmation_email_subject.txt',
                {'custom_quote':custom_quote}
            )
            customer_body = render_to_string(
                'quoting/confirmation_emails/customer_confirmation_email_body.txt',
                {'custom_quote':custom_quote, 'contact_email': settings.CLIENT_FROM_EMAIL}
            )

            # send to customer 
            send_mail(customer_subject, customer_body, settings.CLIENT_FROM_EMAIL, [customer_email])

            client_subject = render_to_string(
                'quoting/confirmation_emails/client_confirmation_email_subject.txt',
                {'custom_quote':custom_quote}
            )
            client_body = render_to_string(
                'quoting/confirmation_emails/client_confirmation_email_body.txt',
                {'custom_quote':custom_quote}
            )
            # send to client/website owner 
            send_mail(client_subject, client_body, settings.CLIENT_FROM_EMAIL, [settings.CLIENT_FROM_EMAI])

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
