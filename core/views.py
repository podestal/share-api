from django.shortcuts import render
from django.http import HttpResponseRedirect   

def activate(request, uid, token):
    return HttpResponseRedirect(f'http://localhost:5173/activate/{uid}/{token}')

def reset_password(request, uid, token):
    return HttpResponseRedirect(f'http://localhost:5173/reset_new/{uid}/{token}')
