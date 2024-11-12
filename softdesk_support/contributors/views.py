from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Contributor
from .serializers import ContributorSerializer
from softdesk_support.permissions import IsAuthenticated, IsContributor, IsAuthor


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
