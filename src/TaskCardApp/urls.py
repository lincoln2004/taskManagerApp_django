
from django.urls import path

from .views.taskcard import interface, createtask, mytasks

from .views.group import listgroup, signUpGroup, creategroup, invitegroup

urlpatterns = [
    path('taskcards', interface.interfaceTaskCard, name='taskcards'),
    path('createTask', createtask.createTaskCard, name='createtask'),
    
    path('mytasks', mytasks.myTaskCard, name='mytasks'),
    path('mytasks/updatecard/<int:id>', mytasks.updateCard, name='updateAction'),
    path('mytasks/deletecard/<int:id>', mytasks.deleteCard,name='deleteAction'),
    
    path('groups', listgroup.listGroups, name='grouplist'),
    path('groups/create', creategroup.createGroup, name='creategroup'),
    path('groups/<str:group_name>', invitegroup.inviteGroup, name='inviteGroup'),
    path('groups/add/<str:group_name>', signUpGroup.signUpGroup, name='addgroup')
]