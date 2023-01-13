from django.http import HttpRequest
from django.shortcuts import render

from ...models import taskcard

from ...forms import FilterTaskCardForm
from Auth.middleware import authMiddleware

from datetime import date

@authMiddleware
def interfaceTaskCard(req: HttpRequest):
    
    form = FilterTaskCardForm(user=req.user)    
    
    tasks = taskcard.objects.filter(group__members=req.user)
    
    if req.GET.get('group', False):
        
        form = FilterTaskCardForm(req.user, req.GET)
        
        if form.is_valid():
            
            if form.cleaned_data.get('group') == 'all':
                
                pass
            
            else:
                
                tasks = tasks.filter(group__name = form.cleaned_data.get('group'))   
                
    if req.GET.get('dateExp', False):
        
        form = FilterTaskCardForm(req.user, req.GET)
                    
        if form.is_valid():
            
           if form.cleaned_data.get('dateExp') == 'expired':
               
            tasks = tasks.filter(deadline__lte=date.today())
           
           elif form.cleaned_data.get('dateExp') == 'on_deadline':
               
               tasks = tasks.filter(deadline__gte=date.today()) 
               
           else:
               
               pass    
    
    tasks = tasks[::-1]           
               
    for task in tasks:
        
        task.deadline = task.deadline.strftime('%d/%m/%Y')            
    
    return render(req, 'taskcards.html', {'tasks': tasks, 'filter': form})
