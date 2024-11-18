from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer
from issues.models import Issue
from softdesk_support.permissions import CommentPermission


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    def get_queryset(self):
        """Get comments an issue."""
        issue_id = self.kwargs.get('issue_pk')
        if issue_id:
            return Comment.objects.filter(issue__id=issue_id)
        return Comment.objects.none()

    def get_serializer_context(self):
        """Add issue to serializer context."""
        context = super().get_serializer_context()
        issue_id = self.kwargs.get('issue_pk')
        if issue_id:
            issue = Issue.objects.get(id=issue_id)
            context['issue'] = issue
        return context

    def perform_create(self, serializer):
        """Create a comment."""
        issue = Issue.objects.get(id=self.kwargs['issue_pk'])
        serializer.save(author=self.request.user, issue=issue)
