from django.urls import include, path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path("", lambda req: redirect('/'), name="account"),
    path("", views.todo_list, name="todo"),
]