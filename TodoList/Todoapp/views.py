from django.shortcuts import render
from Todoapp.models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        print("Пришли данные")
        if "task" in request.POST:
            print(request.POST["task"])
            # Создание новой записи
            new_task = Task(text=request.POST["task"])
            # Сохранение новой записи
            new_task.save()

    tasks = Task.objects.all()
    context = {
        "title": "TODO list",
        "tasks": tasks
    }
    return render(request, "index.html", context) 
