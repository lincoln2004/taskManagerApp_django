from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm



def loginRoute(req: HttpRequest):
    
    form = LoginForm()
    
    if req.method == 'POST':
        
        form = LoginForm(req.POST)
        
        if form.is_valid():
            
            data: dict = form.cleaned_data
            
            result = authenticate(req, username=data.get('username', False), password=data.get('pwd', False))
            
            if result is not None:
                
                login(req, result)
                
                print(reverse('taskcards'))
                
                return redirect(reverse('taskcards'))
    
    
    return render(req,'login.html', {'form': form, 'post_form': 'login'})


def register(req: HttpRequest):
    
    form = RegisterForm()
    
    if req.method == 'POST':
        
        form = RegisterForm(req.POST)
        
        if form.is_valid():
            
            data: dict = form.cleaned_data
            
            try:
                User.objects.get(username=data.get('username'))
            
            except User.DoesNotExist:
                
                try:
                    User.objects.create_user(data.get('username'), None, data.get('pwd'))
                
                except:
                    return render(req,'register.html', {'form': form, 'post_form': 'register'})               
    
    return render(req,'register.html', {'form': form, 'post_form': 'register'})


def logoutRoute(req: HttpRequest):
    
    logout(req)
    
    return redirect(reverse('login'))