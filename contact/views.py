from django.shortcuts import render, resolve_url as r
from django.http import HttpResponseRedirect, Http404
from contact.forms import ContactForm
from django.core import mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from contact.models import Contact

def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})

    contact = Contact.objects.create(**form.cleaned_data)

    _send_mail(
        'contact/contact_email.txt',
        {'contact': contact},
        'Mensagem enviada!',
        settings.DEFAULT_FROM_EMAIL,
        contact.email
    )
    
    messages.success(request, 'Mensagem enviada com sucesso!')
    return HttpResponseRedirect('/contact/')

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})

def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])