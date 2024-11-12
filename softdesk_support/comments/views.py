from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Comments
from .serializers import CommentSerializer
from  softdesk_support.permissions import IsAuthenticated, IsContributor, IsAuthor


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
