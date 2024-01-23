from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    template = loader.get_template("todo/todo_list.html")
    context = {}
    return HttpResponse(template.render(context, request))