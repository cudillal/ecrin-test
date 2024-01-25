from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title']