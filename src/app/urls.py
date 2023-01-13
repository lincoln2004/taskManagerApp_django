
from django.urls import path, include

from django.shortcuts import redirect

def page(req):
    
    return redirect('login')

urlpatterns = [
    path('', include('TaskCardApp.urls')),
    path('', include('Auth.urls')),
    path('', page)
]
