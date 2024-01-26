from django.contrib.auth.models import User
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        """
        Prevent adding tasks using the REST API for other users.
        Required because POST requests don't trigger has_object_permission().
        """
        if request.method == 'POST':
            if 'owner' in request.data:
                owner_id = request.data['owner']
                if owner_id is not None:
                    return str(owner_id) == str(request.user.id)
            return False
        return True

    def has_object_permission(self, request, view, obj):
        """
        Allow GET, HEAD or OPTIONS requests.
        """
        return (request.method in permissions.SAFE_METHODS)