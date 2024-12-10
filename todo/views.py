from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo

# Create your views here.
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')

        if title:
            ToDo.objects.create(title=title)
            return redirect('task_list')
    return render(request, 'add_task.html')

def all_tasks(request):
    tasks = ToDo.objects.all()
    return render(request, 'task_list.html', {"tasks": tasks})

def delete_task(request, task_id):
    task = get_object_or_404(ToDo, id=task_id)
    task.delete()
    return redirect('task_list')


