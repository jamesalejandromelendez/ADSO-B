from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import proyect, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask
from .forms import CreateNewProject
# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request, "index.html", {'title':title})

def about(request):
    username = 'fazt'
    return render(request, "about.html", {'username':username})

def hello(request, username):
    return HttpResponse('<p> Hola %s</p>' % username)

def projects(request):
    # projects = list(proyect.objects.values())
    projects = proyect.objects.all()
    return render(request, "projects/projects.html",{'projects':projects})

def tasks(request):
    # task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {'tasks': tasks})


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        form = CreateNewTask(request.POST)
        if form.is_valid():
            Task.objects.create(title=form.cleaned_data['title'], description=form.cleaned_data['description'], proyect_id=2)
            return redirect('/tasks/')
        else:
            return render(request, 'tasks/create_task.html', {'form': form})
    

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:
        proyect.objects.create(name=request.POST["name"])
        return redirect('/projects/')

