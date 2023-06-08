from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()          #Pobiera wszystkie obiekty Task z bazy danych
    
    form = TaskForm()          

    if request.method == 'POST':        #Sprawdzanie czy jest żadanie typu POST
        form = TaskForm(request.POST)   #Przypisanie do zmiennej dane z żadania POST jako argument
        if form.is_valid():             #Sprawdzainie czy przeszło walidacje
            form.save()                 #Zapisuje dane w bazie danych
        return redirect('/')         

    context = {
        'tasks': tasks,
        'form': form     
    }
    return render(request, 'tasks/index.html', context)


def update_task(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form' : form
    }

    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect("/")

    context = {
        "item": item
    }

    return render(request, 'tasks/delete.html', context)