from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from softdesk_support.permissions import ProjectPermission
from .models import Project
from contributors.models import Contributor
from .serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectListViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing projects.
    """
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, ProjectPermission]

    def get_serializer_class(self):
        """Choose serializer based on action."""
        if self.action == 'list':
            return ProjectListSerializer
        elif self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectDetailSerializer

    def perform_create(self, serializer):
        """Create a new project."""
        project = serializer.save(author=self.request.user)

        Contributor.objects.create(
                user=self.request.user,
                project=project,
                role="Owner"
            )
