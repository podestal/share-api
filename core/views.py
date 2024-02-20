from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, mail_admins, EmailMessage, BadHeaderError
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
    return HttpResponseRedirect(f'http://myshare-web.s3-website-us-east-1.amazonaws.com/activate/{uid}/{token}')

def reset_password(request, uid, token):
    return HttpResponseRedirect(f'http://myshare-web.s3-website-us-east-1.amazonaws.com/reset_new/{uid}/{token}')