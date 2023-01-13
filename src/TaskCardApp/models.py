from django.db import models
from django.contrib.auth.models import User

import time
import random
import secrets

# Create your models here.

class groups(models.Model):
    
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='members')
    group_key = models.CharField(max_length=60) 
    
    def save(self, *args, **kargs):
        
        self.group_key = secrets.token_hex()[-50:] + str(round( 10 ** 10 * time.time() * random.random()))[-10:]
        
        super(groups, self).save(*args, **kargs)
        
    
    def __repr__(self) -> str:
        return self.name
        

class taskcard(models.Model):
    
    author = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300, null=False)
    title = models.CharField(max_length=150, null=False)
    
    
    emited = models.DateField(auto_now=True)
    deadline = models.DateField(null=True)  
    
    group = models.ForeignKey(groups, on_delete= models.CASCADE, related_name='group')         