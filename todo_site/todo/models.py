from django.db import models
from django.conf import settings


class Task(models.Model):
    """
    Task model - title and foreign key to User object
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title