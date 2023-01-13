from django.http import HttpRequest
from django.shortcuts import render, redirect

from ...models import taskcard, groups

from ...forms import CreateTcForm
from Auth.middleware import authMiddleware


@authMiddleware
def createTaskCard(req: HttpRequest):
    
    form = CreateTcForm(user= req.user)
    
    if req.method == 'POST':
        
        form = CreateTcForm(req.user, req.POST)
        
        if form.is_valid():
            
            body: dict = form.cleaned_data
            keys = ('groups','description','title','deadline')
            
            body = dict( [ [key, body.get(key)] for key in keys 
                          if body.get(key, False) != False and body.get(key, False) != '' ])
            
            if body.get('groups') == 'empty':
                
                body['groups'] = False
                
            if body.get('groups'):    
            
                body['groups'] = groups.objects.get(id=body.get('groups')) 
                
            else:
                return redirect('createtask')
            
            
            try:
                
                taskcard.objects.get(title=body.get('title'), author=body.get('author'))
            
            except taskcard.DoesNotExist:  
                
                print(body)
                 
                taskcard.objects.create(author=req.user.username, description=body.get('description'), 
                                        title=body.get('title'), deadline=body.get('deadline'), group= body.get('groups')) 
                
            return redirect('taskcards')
    
    
    return render(req, 'createtask.html', {'form': form, 'exist': False, 'post_url': 'createtask'})
