from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Task

def todos(request):
    day = datetime.today()
    tasks = Task.objects.all()
    context = {
        'todo_list': tasks,
    }
    return render(request, 'todo_list.html', context)
def completed_todos(request, index):
    cur_day = datetime.today()
    tasksed = Task.objects.all()[int(index)-1]
    context = {
        'task': tasksed
    }
    return render(request, 'completed_todo_list.html', context)