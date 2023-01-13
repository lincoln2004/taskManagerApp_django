from django.shortcuts import redirect
from django.http import HttpRequest

from ...forms import  creategroupForm
from ...models import groups

from Auth.middleware import authMiddleware



@authMiddleware
def createGroup(req:HttpRequest):
     
    if req.method == 'POST':
    
       form = creategroupForm(req.POST)
       
       if form.is_valid():
           
        data: dict = form.cleaned_data
           
        
        if data.get('name', False):
            group = groups.objects.create(name= data.get('name'))
            
            group.members.add(req.user)       
            
            group.save()
            
    
    return redirect('grouplist')