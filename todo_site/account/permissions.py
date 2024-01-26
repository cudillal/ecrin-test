from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    """
    Read only permission for users REST API.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS