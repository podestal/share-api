from django.shortcuts import render
from django.http import HttpResponseRedirect   

def say_hello(request, uid, token):
    print(uid)
    print(token)
    # return render(request, 'reset.html', {'uid': uid,'token': token})
    return HttpResponseRedirect(f'http://localhost:5173/reset_new/{uid}/{token}')
