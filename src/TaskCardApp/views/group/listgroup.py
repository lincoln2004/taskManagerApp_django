from django.shortcuts import render
from django.http import HttpRequest

from ...forms import  groupFilterForm
from ...models import groups

from Auth.middleware import authMiddleware



@authMiddleware
def listGroups(req: HttpRequest):
    
    groupslist = groups.objects.all()
    
    if req.GET.get('search', False):
        
        groupslist = groups.objects.filter(name__contains= req.GET.get('search'))
        
    filter = req.GET.get('filter', False)    
    
    if filter:
        
        if filter == 'part':
            
            groupslist = groups.objects.filter(members__username = req.user)
            
        elif filter == 'not_part':
                
            groupslist = groups.objects.exclude(members__username = req.user)
        
        else:
            groupslist    
            
            
    for item in groupslist:
        
        if item.members.contains(req.user):
            
            item.part = True
            
        else :
            item.part = False         
    
    return render(req, 'group/group.html', {'groups': groupslist, 'filter': groupFilterForm()})  

