from django.shortcuts import render, redirect, get_object_or_404
from task.models import Task


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': tasks
    })


def create_view(request):
    task = Task.objects.create(
        name=request.POST.get('name'),
        due_date=request.POST.get('due_date')
    )
    return redirect('index')


def delete_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('index')


def do_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if task.status == 'new':
        task.status = 'process'
        task.due_date = 'due_date'
        task.save()
        return redirect('index')
    elif task.status != 'done' and task.status != 'new':
        task.status = 'done'
        task.due_date = 'due_date'
        task.save()
        return redirect('index')

def update_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        Task.objects.all()
        context = {
            'task': task
        }
        return render(request, 'update.html', context)
    elif request.method == 'POST':
        task.name = request.POST.get('name')
        task.status = request.POST.get('status')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('index')


def filter_view(request):
    tasks = Task.objects.all()
    context={
        'tasks': tasks
        }
    for task in tasks:
    	if task.status == 'done':
    		task.delete()
    return redirect('index')