from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.todo,name="todo"),
    path('delete',views.delete, name="delete"),
    path('add_todos', views.add_todos, name="add_todos"),
    path('get_all', views.get_all, name="get_all"),
]