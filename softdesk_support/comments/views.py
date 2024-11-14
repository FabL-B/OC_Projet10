from rest_framework import viewsets

from .models import Comments
from .serializers import CommentSerializer



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
