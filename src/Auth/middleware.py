from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def authMiddleware(func):
    
    def inner(req: HttpRequest, *args, **kargs):
        
        if req.user and req.user.is_authenticated:
            
            return func(req,*args, **kargs)
        
        
        return redirect(reverse('login'))
    
    
    inner.__name__ = func.__name__
    
    
    return inner