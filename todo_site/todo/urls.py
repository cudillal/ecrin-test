from django.urls import include, path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_main"),
]