import json

from django.contrib.auth.models import User
from rest_framework import permissions

from account.serializers import UserSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            if 'owner' in request.data:
                owner_id = request.data['owner']
                if owner_id is not None:
                    return str(owner_id) == str(request.user.id)
            return False
        return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user