from rest_framework.permissions import BasePermission

from projects.models import Project
from contributors.models import Contributor


class GlobalPermission(BasePermission):
    """
    Base permission class for common helper methods.

    Provides reusable methods for checking if a user is the author of
    an object or a contributor to a project.
    """

    def is_author(self, request, obj=None):
        """Check if the user is the author of the object."""
        return obj and hasattr(obj, 'author') and obj.author == request.user

    def is_contributor(self, request, view):
        """Check if the user is a contributor for the project."""
        project_id = view.kwargs.get('project_pk')
        if not project_id:
            return False
        return Contributor.objects.filter(
            project_id=project_id,
            user=request.user
        ).exists()


class ProjectPermission(GlobalPermission):
    """Permissions specific to projects."""

    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return self.is_contributor(request, view)

        return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return self.is_author(request, obj)

        return False


class ContributorPermission(GlobalPermission):
    """Permissions specific to contributors."""

    def has_permission(self, request, view):
        if view.action == 'list':
            return self.is_contributor(request, view)
        elif view.action == 'create':
            project_id = view.kwargs.get('project_pk')
            project = Project.objects.get(id=project_id)
            return project.author == request.user
        elif view.action == 'destroy':
            return True

        return False

    def has_object_permission(self, request, view, obj):
        project = obj.project
        return self.is_author(request, project)


class CommentPermission(GlobalPermission):
    """Permissions specific to comments."""

    def has_permission(self, request, view):
        if view.action in ['list',
                           'create',
                           'retrieve',
                           'update',
                           'partial_update',
                           'destroy'
                           ]:
            return self.is_contributor(request, view)

        return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return self.is_author(request, obj)

        return False


class IssuePermission(GlobalPermission):
    """Permissions specific to issues."""

    def has_permission(self, request, view):
        if view.action in ['list',
                           'create',
                           'retrieve',
                           'update',
                           'partial_update',
                           'destroy'
                           ]:
            return self.is_contributor(request, view)

        return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return self.is_author(request, obj)

        return False
