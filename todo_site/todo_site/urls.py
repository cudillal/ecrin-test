"""
URL configuration for todo_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from account.views import UserViewSet
from todo.views import TaskViewSet


# REST API routes
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", include("account.urls")),  # Account app
    path("todo/", include("todo.urls")),  # Todo app
]