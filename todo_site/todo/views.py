import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from rest_framework import permissions, viewsets

from .forms import TaskForm
from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer
from .login_decorator import login_required_message


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        current_user = self.request.user
        return Task.objects.filter(owner=current_user.id)


@login_required
def task_list(request):
    return render(request, 'todo/task_list.html', {
        'tasks': Task.objects.filter(owner=request.user.id),
    })

@login_required_message
@login_required
@never_cache
def todo_list(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Logged out successfully.')
        return redirect('/')
    else:
        template = loader.get_template("todo/todo_list.html")
        tasks = []
        try:
            tasks = Task.objects.filter(owner=request.user)
        except ObjectDoesNotExist:
            pass
        context = {'user': request.user,
                   'tasks': tasks,
                   'add_form': TaskForm(),
                   'edit_form': TaskForm(),
                   'delete_form': TaskForm()}
        return HttpResponse(template.render(context, request))

@login_required
def add_task(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'todo/add_task.html', {
            'form': form,
        })
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_bound and form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "todoListChanged": None,
                        "showMessage": "Task added successfully."
                    })
                }
            )

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, "todo/edit_task.html", {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST, instance=task)
        if form.is_bound and form.is_valid():
            form.save()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "todoListChanged": None,
                    "showMessage": "Task edited successfully."
                })
            }
        )

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, "todo/delete_task.html", {'form': form})
    elif request.method == 'POST':
        task.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "todoListChanged": None,
                    "showMessage": f"Task '{task.title}' deleted successfully."
                })
            }
        )