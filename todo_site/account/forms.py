from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    prefix = "login"
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class RegisterForm(UserCreationForm):
    prefix = "register"
    display_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=32, help_text='Display name (32 characters max.)', error_messages={"required": "Please enter your name to be displayed."})
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=64, help_text='Enter a valid email address')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields = ['display_name', 'username','email','password1','password2']