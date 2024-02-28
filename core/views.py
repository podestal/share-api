from django.shortcuts import HttpResponse
from django.core.mail import BadHeaderError
from django.http import HttpResponseRedirect   
from templated_mail.mail import BaseEmailMessage

def payment_confirmation(request, email):
    try:
        message = BaseEmailMessage(
            template_name='emails/payment.html',
        )
        message.send([email])
    
    except BadHeaderError:
        pass
    return HttpResponse('Ok') 

def activate(request, uid, token):
    return HttpResponseRedirect(f'https://myshares-web.com/activate/{uid}/{token}/')

def reset_password(request, uid, token):
    return HttpResponseRedirect(f'https://myshares-web.com/reset_new/{uid}/{token}/')