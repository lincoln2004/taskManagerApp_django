from django.shortcuts import render, redirect
from django.http import HttpRequest

from ...models import groups

from Auth.middleware import authMiddleware


@authMiddleware
def inviteGroup(req:HttpRequest, group_name: str):
    
    
    if group_name:
        
        group = groups.objects.get(name=group_name)
        
        if group is not None:
            
            try:
                if group.members.get(username=req.user) is not None:
                
                   return render(req, 'group/token.html', {'group': group})
            
            except :
                
                pass
    
    
    return redirect('grouplist')