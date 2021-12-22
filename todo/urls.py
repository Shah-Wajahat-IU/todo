from django.urls import path
from . views import index,addTodoForm,completeTodo,deleteCompleted,allDeleted
urlpatterns = [
    path("",index,name="index"),
    path("add",addTodoForm,name="add"),
    path("completed/<todo_id>",completeTodo,name="completed"),
    path("deletecompleted",deleteCompleted,name="deletecompleted"),
    path("deleteall",allDeleted,name="deleteall"),
    
    ]
