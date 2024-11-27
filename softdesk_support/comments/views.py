from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .serializers import CommentSerializer, CommentListSerializer
from issues.models import Issue
from softdesk_support.permissions import CommentPermission


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.

    Provides functionality to list, retrieve, create, update, and delete
    comments for a specific issue.
    """
    permission_classes = [IsAuthenticated, CommentPermission]

    def get_queryset(self):
        """Return the queryset of comments for a specific issue."""
        issue_id = self.kwargs.get('issue_pk')
        if issue_id:
            return Comment.objects.filter(issue__id=issue_id)
        return Comment.objects.none()

    def get_serializer_context(self):
        """Add the issue instance to the serializer context."""
        context = super().get_serializer_context()
        issue_id = self.kwargs.get('issue_pk')
        if issue_id:
            issue = Issue.objects.get(id=issue_id)
            context['issue'] = issue
        return context

    def get_serializer_class(self):
        """Choose serializer based on action."""
        if self.action == 'list':
            return CommentListSerializer
        elif self.action == 'retrieve':
            return CommentSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        """Create a new comment for a specific issue."""
        issue = Issue.objects.get(id=self.kwargs['issue_pk'])
        serializer.save(author=self.request.user, issue=issue)
