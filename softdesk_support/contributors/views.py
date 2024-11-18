from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contributor
from .serializers import ContributorSerializer
from projects.models import Project
from softdesk_support.permissions import ContributorPermission


class ContributorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing contributors.

    Provides functionality to list, retrieve, add, update, and delete
    contributors for a specific project.
    """
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, ContributorPermission]

    def get_queryset(self):
        """Return the queryset of contributors for a specific project."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Contributor.objects.filter(project__id=project_id)
        else:
            Contributor.objects.none()

    def perform_create(self, serializer):
        """Add a contributor to a specified project."""
        project = Project.objects.get(id=self.kwargs['project_pk'])
        user = serializer.validated_data.get('user')
        serializer.save(project=project, user=user)
