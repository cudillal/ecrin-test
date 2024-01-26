from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    User class serializer for the REST API.
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email']