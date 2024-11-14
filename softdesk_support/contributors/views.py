from rest_framework import viewsets

from .models import Contributor
from .serializers import ContributorSerializer
from projects.models import Project
from softdesk_support.permissions import ContributorPermission


class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermission]


    def get_queryset(self):
        """Get contributors from a specified project."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Contributor.objects.filter(project__id=project_id)  
        else:
            Contributor.objects.none()

    def perform_create(self, serializer):
        """Add a contributor to a specified project."""
        project = Project.objects.get(id=self.kwargs['project_pk'])
        # A voir si seul l'author du projet peut ajouter un contributor
        # ou si un contributor de projet peut egalment le faire
        user = serializer.validated_data.get('user')
        serializer.save(project=project, user=user)
