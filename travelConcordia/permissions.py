# travelConcordia/permissions.py
from rest_framework import permissions

class IsAgentOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow agents to edit the data.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to agents.
        return request.user and request.user.is_agent
