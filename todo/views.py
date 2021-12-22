from django import forms
import django
from django.shortcuts import render,redirect
from .models import TodoList
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_list=TodoList.objects.order_by('id')
    form= TodoListForm()
    
    context={"todo_list":todo_list,'form':form}
    return render(request,"todolist/index.html",context)
@require_POST
def addTodoForm(request):
    form= TodoListForm(request.POST)
    if form.is_valid():
        new_todo=TodoList(text=request.POST['text'])
        new_todo.save()
    print(request.POST['text'])

    return redirect('index')