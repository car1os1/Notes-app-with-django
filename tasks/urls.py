from asyncio import create_task
from django import views
from django.urls import  path
from .views import delete_task, list_tasks,create_task


urlpatterns  =[
    path('',list_tasks),
    path('new/',create_task,name='create_task'),
    path('delete_task/<int:task_id>/',delete_task,name='delete_task')
]