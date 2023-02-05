from ..models import User
from django.shortcuts import redirect

def islogin_required(vista):
    def wrapper(request,*args,**kwargs):
        if request.session.get('username') is None:
            return redirect('login')                 
        return vista(request,*args,**kwargs)
    return wrapper