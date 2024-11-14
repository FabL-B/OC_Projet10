from rest_framework import viewsets

from softdesk_support.permissions import ProjectPermission
from .models import Project
from contributors.models import Contributor
from .serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectListViewSet(viewsets.ModelViewSet):
    """Handle listing of all projects."""
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    permission_classes = [ProjectPermission]

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)

        Contributor.objects.create(
                user=self.request.user,
                project=project,
                role="Owner"
            )


class ProjectDetailViewSet(viewsets.ModelViewSet):
    """Handle CRUD on a specified project"""
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [ProjectPermission]
