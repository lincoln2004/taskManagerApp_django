from django.shortcuts import render, redirect
from django.http import HttpRequest

from ...forms import UpdateTcForm
from ...models import taskcard

from Auth.middleware import authMiddleware

from datetime import date
import re



@authMiddleware
def myTaskCard(req: HttpRequest):
    
    tasks = taskcard.objects.filter(author= req.user)
    
    for task in tasks:
        
        task.description = re.findall('^(?:\S+\s+\n?){1,3}', task.description)[0] + ' ...'
        task.deadline = date.strftime(task.deadline,'%d/%m/%Y')
    
    return render(req, 'mytasks.html', {'tasks': tasks})



@authMiddleware
def deleteCard(req: HttpRequest, id: int):
    
    if id :
        
        try:
            
            taskcard.objects.get(id=id).delete()
            
        except taskcard.DoesNotExist:
            
            pass 
            
        return redirect('mytasks')      
    
    
@authMiddleware
def updateCard(req: HttpRequest, id: int):
   
   form = UpdateTcForm() 
    
   if req.method == 'POST':
       
       form = UpdateTcForm(req.POST) 
       
       if form.is_valid():
        
        tmp: dict = form.cleaned_data
       
       
        if not id:
           
          return redirect('mytasks')
       
        task = taskcard.objects.get(id= id)  
        
        if task is not None:
            
            keys = [ 'description', 'deadline', 'title'] 
                
            for key in keys:
                    
                setattr(task, key, tmp.get(key) or getattr(task, key))
                    
            task.save()     
            
            return redirect('mytasks')   
                
            
   return render(req, 'updatetask.html', { 'form': form, 'task': id or False})
