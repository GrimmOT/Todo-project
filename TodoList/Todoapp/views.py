from django.shortcuts import render
from Todoapp.models import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {
        "title": "TODO list",
        "tasks": tasks
    }
    return render(request, "index.html", context) 
