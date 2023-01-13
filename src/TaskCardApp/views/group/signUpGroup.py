from django.shortcuts import render, redirect
from django.http import HttpRequest

from ...forms import  joingroupForm
from ...models import groups

from Auth.middleware import authMiddleware


@authMiddleware
def signUpGroup(req:HttpRequest, group_name:str):
    
    if group_name:
        
        group = groups.objects.get(name=group_name)
        
        if group is not None:
            
            if group.members.contains(req.user):
                
                return redirect('grouplist')
            
            form = joingroupForm()
            
            if req.method == 'POST':
                
                form = joingroupForm(req.POST)
                
                
                if form.is_valid():
                    
                   invite = form.cleaned_data.get('invitetoken')  
                   
                   if invite:
                      
                    if group.group_key == invite:
                          
                       group.members.add(req.user) 
                       
                       return redirect('grouplist')    
                
            
            return render(req, 'group/addgroup.html', {'group': group.name, 'form': form})
        
        
    return redirect('grouplist')  