from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    """Permission that grant access if user is author of the ressource."""

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user
        
        return True


class IsContributor(BasePermission):
    """Permission that grant access to contributors."""
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.contributors.filter(user=request.user).exists()


class IsAuthenticated(BasePermission):
    """Permission that grant access if user is user is authenticated."""
    def has_permission(self, request, view):
        return request.user.is_authenticated
