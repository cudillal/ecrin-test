from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        template = loader.get_template("todo/todo_list.html")
        context = {'user': request.user}
        return HttpResponse(template.render(context, request))