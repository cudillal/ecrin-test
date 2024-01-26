from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    """
    Task class serializer for REST API.
    """
    class Meta:
        model = Task
        fields = ['url', 'owner', 'title']