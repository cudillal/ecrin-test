from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def index(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('todo')
        else:
            template = loader.get_template("account/index.html")
            context = {'form': register_form}
            return HttpResponse(template.render(context, request))
    else:
        register_form = RegisterForm()
        template = loader.get_template("account/index.html")
        context = {'form': register_form}
        return HttpResponse(template.render(context, request))
