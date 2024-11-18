from rest_framework import viewsets

from .models import Issue
from .serializers import IssueSerializer
from projects.models import Project
from softdesk_support.permissions import IssuePermission


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IssuePermission]

    def get_queryset(self):
        """Get issues from a project."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Issue.objects.filter(project__id=project_id)
        return Issue.objects.none()

    def get_serializer_context(self):
        """Add project to serializer context."""
        context = super().get_serializer_context()
        context['project'] = Project.objects.get(id=self.kwargs['project_pk'])
        return context

    def perform_create(self, serializer):
        """Create an issue."""
        project = Project.objects.get(id=self.kwargs['project_pk'])
        serializer.save(project=project, author=self.request.user)
