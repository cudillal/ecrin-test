from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Task(models.Model):
    # TODO: change foreign key
    #owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    add_date = models.DateTimeField("Date added")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title