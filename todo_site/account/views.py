from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from .forms import LoginForm, RegisterForm
from .permissions import ReadOnly
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    REST API endpoint that allows users to view their own information.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ReadOnly]

    def get_queryset(self):
        """
        Allow for logged in user to view their own information only.
        """
        current_user = self.request.user
        return User.objects.filter(id=current_user.id)


def _stay_on_page(request, login_form, register_form):
    """
    Render the login/register page again (called if the form doesn't validate).
    """
    template = loader.get_template("account/index.html")
    return HttpResponse(template.render({'login_form': login_form, 'register_form': register_form}, request))

def _redirect_to_todo(request, user):
    """
    Redirect to todo list (called if login or registration is successful).
    """
    login(request, user)
    return redirect('todo_main')

def index(request):
    """
    Handle main view rendering and form POST requests.
    """
    log_in = False
    login_form = None
    register_form = None

    if request.method == 'POST':
        # Login form
        if LoginForm.prefix in request.POST:
            login_form = LoginForm(data = request.POST)
            if login_form.is_bound and login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    log_in = True
                    messages.success(request, 'Logged in successfully.')
            else:
                messages.error(request, 'The username and password combination is incorrect.')
        # Registration form
        elif RegisterForm.prefix in request.POST:
            register_form = RegisterForm(data = request.POST)
            if register_form.is_bound and register_form.is_valid():
                user = register_form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'Signed up successfully. You are now logged in.')
                user = authenticate(username=register_form.cleaned_data['username'].lower(),
                                    password=register_form.cleaned_data['password1'],
                                    )
                log_in = True

    if log_in:
        return _redirect_to_todo(request, user)
    else:  # First time loading page (GET) or invalid form (POST)
        if login_form is None:
            login_form = LoginForm()
        if register_form is None:
            register_form = RegisterForm()
        
        return _stay_on_page(request, login_form, register_form)