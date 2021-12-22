from django.urls import path
from . views import index,addTodoForm
urlpatterns = [
   
    path("",index,name="index"),
    
    path("add",addTodoForm,name="add"),
]
