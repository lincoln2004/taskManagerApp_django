from django import forms
from .models import groups

class CreateTcForm(forms.Form):
    
    title = forms.CharField(widget= forms.TextInput({'placeholder': 'title'}), label='Title:')
    deadline = forms.DateField(widget= forms.DateInput( {'type': 'date'}), label='Deadline:')
    
    description = forms.CharField(label='Description:', widget= forms.Textarea)
    groups = forms.ChoiceField(choices=[('empty','you are not take any group')])
    
    def __init__(self, user=None, *args, **kargs):
        
        super().__init__( *args, **kargs)
        
        tmp = [ (el.id,el.name ) for el in groups.objects.filter(members__username=user)]
        
        self.fields['groups'].choices = tmp if tmp.__len__() > 0 else [('empty','you are not take any group')]
    

class UpdateTcForm(forms.Form):
    
    title = forms.CharField(widget=forms.TextInput({ 'placeholder': 'title'}) ,label='Title:', required=False)
    deadline = forms.DateField(widget=forms.DateInput({'type': 'date'}), label='Deadline:', required=False)
    
    description = forms.CharField( widget= forms.Textarea({ 'placeholder': 'description'}), label='Description:', required=False)    
    

class FilterTaskCardForm(forms.Form):
    
    group = forms.ChoiceField(choices=[('all', 'all the groups')], label='Group:')
    dateExp = forms.ChoiceField(choices=[('all', 'all the dates')], label='Date:')
    
    def __init__(self, user=None, *args, **kargs):
        
        super().__init__( *args, **kargs)
        
        tmp = [('all', 'all the groups')]
        
        tmp.extend([ (el.name, el.name ) for el in groups.objects.filter(members__username=user)])
        
        self.fields['group'].choices = tmp if tmp.__len__() > 1 else tmp  
        self.fields['group'].initial = ('all the groups')
        
        tmp = [('all', 'all the dates'), ('expired', 'deadline passed'), ('on_deadline', 'on deadline')]
        
        self.fields['dateExp'].choices = tmp 
        self.fields['dateExp'].initial = ('all the dates')
        
        
        
class groupFilterForm(forms.Form):
    
    filter_choices= [ ('all', 'all the groups'), ('part','make part of group'), ('not_part','part not of group')]          
    
    filter = forms.ChoiceField(choices=filter_choices, label='Group:')
    
        
class creategroupForm(forms.Form):
    
    name = forms.CharField(max_length=100)                
      
      
class joingroupForm(forms.Form):
    
    invitetoken = forms.CharField(max_length=100, label='Invite: ')      