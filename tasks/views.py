from django.shortcuts import redirect, render
from .models import tasks


# Create your views here.
def list_tasks (request):
    task=tasks.objects.all()
    return render(request,'list_tasks.html',{'tasks':task})

def create_task(request):
    task= tasks(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request,task_id):
    task=tasks.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
