from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Issue
from .serializers import IssueSerializer
from softdesk_support.permissions import IsAuthenticated, IsContributor, IsAuthor


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
