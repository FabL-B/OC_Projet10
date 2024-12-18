from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Issue
from .serializers import IssueSerializer, IssueListSerializer
from projects.models import Project
from softdesk_support.permissions import IssuePermission


class IssueViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing issues.

    Provides functionality to list, retrieve, create, update, and delete
    issues for a specific project.
    """
    permission_classes = [IsAuthenticated, IssuePermission]

    def get_queryset(self):
        """Return the queryset of issues for a specific project."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Issue.objects.filter(project__id=project_id)
        return Issue.objects.none()

    def get_serializer_context(self):
        """Add the project instance to the serializer context."""
        context = super().get_serializer_context()
        context['project'] = Project.objects.get(id=self.kwargs['project_pk'])
        return context

    def get_serializer_class(self):
        """Choose serializer based on action."""
        if self.action == 'list':
            return IssueListSerializer
        elif self.action == 'retrieve':
            return IssueSerializer
        return IssueSerializer

    def perform_create(self, serializer):
        """Create a new issue for a specific project."""
        project = Project.objects.get(id=self.kwargs['project_pk'])
        serializer.save(project=project, author=self.request.user)
