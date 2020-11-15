from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import * 

def index(request):
    tasks = Tasks.objects.all()

    form = Task_Forms()
    
    if request.method == 'POST':
        form = Task_Forms(request.POST)  
        if form.is_valid():
            form.save()
        return redirect('/')     

    content = {'tasks':tasks, 'form':form}
    return render(request, 'list/tasks.html', content)

def update_task(request, primkey):
    task = Tasks.objects.get(id=primkey)

    form = Task_Forms(instance=task)

    if request.method == 'POST':
        form = Task_Forms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    content = {'form':form}

    return render(request, 'list/update_tasks.html', content)

def delete_tasks(request, primkey):
    item = Tasks.objects.get(id=primkey)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
        

    content = {'item':item}
    return render(request, 'list/delete.html', content)
