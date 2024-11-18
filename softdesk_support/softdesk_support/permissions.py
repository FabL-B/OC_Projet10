from rest_framework.permissions import BasePermission

from projects.models import Project


class GlobalPermission(BasePermission):
    """Base permission class for common helper methods."""

    def is_author(self, request, obj=None):
        """Check if the user is the author of the object."""
        return obj and hasattr(obj, 'author') and obj.author == request.user

    def is_contributor(self, request, project):
        """Check if the user is a contributor to the project."""
        return project.contributors.filter(user=request.user).exists()


class ProjectPermission(GlobalPermission):
    """Permissions specific to projects."""

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return self.is_contributor(request, obj) or self.is_author(request, obj)
        elif view.action in ['update', 'partial_update', 'destroy']:
            return self.is_author(request, obj)

        return False


class ContributorPermission(GlobalPermission):
    """Permissions specific to contributors."""

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            project_id = view.kwargs.get('project_pk')
            project = Project.objects.get(id=project_id) if project_id else None
            return project and project.author == request.user
        elif view.action == 'destroy':
            return True

        return False

    def has_object_permission(self, request, view, obj):
        project = obj.project

        if view.action == 'destroy':
            return self.is_author(request, project)

        return False


class CommentPermission(GlobalPermission):
    """Permissions specific to comments."""

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        project = obj.issue.project

        if view.action == 'retrieve':
            return self.is_contributor(request, project)
        elif view.action in ['update', 'partial_update', 'destroy']:
            return self.is_author(request, obj)

        return False


class IssuePermission(GlobalPermission):
    """Permissions specific to issues."""

    def has_permission(self, request, view):

        if view.action == 'list':
            return True
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        project = obj.project

        if view.action == 'retrieve':
            return self.is_contributor(request, project)
        elif view.action in ['update', 'partial_update', 'destroy']:
            return self.is_author(request, obj)

        return False
