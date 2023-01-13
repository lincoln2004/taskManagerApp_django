from django.urls import path 
from .views import loginRoute, register, logoutRoute

urlpatterns = [
    
    path('login/', loginRoute, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutRoute, name='logout')
]