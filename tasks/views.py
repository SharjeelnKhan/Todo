from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm, UpdateTaskForm

# Create your views here.


@login_required(login_url='login')
def home(request):
    task = Task.objects.all()

    context = {'task': task}
    return render(request, 'tasks/dashboard.html', context)


def addtask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'tasks/add_task_form.html', context)


def deletetask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task': task}
    return render(request, 'tasks/delete_task.html', context)


def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    form = UpdateTaskForm(request.POST, instance=task)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

