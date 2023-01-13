from django import forms 




class LoginForm (forms.Form):
    
    username = forms.CharField(max_length=100, label='Username:')
    pwd = forms.CharField(label='Password:', widget=forms.PasswordInput)
    
    
class RegisterForm (forms.Form):
    
    username = forms.CharField(max_length=100, label='Username:')
    pwd = forms.CharField(label='Password:')   