from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, mail_admins, EmailMessage, BadHeaderError
from django.http import HttpResponseRedirect   
from templated_mail.mail import BaseEmailMessage

def activate(request, uid, token):
    return HttpResponseRedirect(f'http://localhost:5173/activate/{uid}/{token}')

def reset_password(request, uid, token):
    return HttpResponseRedirect(f'http://localhost:5173/reset_new/{uid}/{token}')

def payment_confirmation(request, email):
    try:
        message = BaseEmailMessage(
            template_name='emails/payment.html',
            context={'name': 'Athos'}
        )
        message.send([email])

    except BadHeaderError:
        pass
    return HttpResponse('Hello') 