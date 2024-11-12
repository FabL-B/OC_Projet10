from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Project
from contributors.models import Contributor
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from softdesk_support.permissions import IsAuthenticated, IsContributor, IsAuthor


class ProjectListViewSet(viewsets.ModelViewSet):
    """Handle listing of all projects."""
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return super().get_permissions()   

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

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        elif self.action == 'retrieve':
            return [IsAuthenticated()]
        return [IsAuthenticated()]
