from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, mail_admins, EmailMessage, BadHeaderError
from django.http import HttpResponseRedirect   
from templated_mail.mail import BaseEmailMessage

def activate(request, uid, token):
    return HttpResponseRedirect(f'http://localhost:5173/activate/{uid}/{token}')

def reset_password(request, uid, token):
    return HttpResponseRedirect(f'http://localhost:5173/reset_new/{uid}/{token}')

def payment_confirmation(request):
    try:
        message = BaseEmailMessage(
            template_name='email/payment.html',
            context={'name': 'Athos'}
        )
        message.send(['l.r.p.2991@gmail.com'])

    except BadHeaderError:
        pass
    return HttpResponse('Hello') 