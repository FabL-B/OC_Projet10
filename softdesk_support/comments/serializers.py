from rest_framework import serializers
from .models import Comment
from issues.models import Issue

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    class Meta:
        model = Comment
        fields = ['id', 'author', 'issue', 'issue_url', 'description', 'created_time']
        read_only_fields = ['id', 'author', 'issue', 'issue_url', 'created_time']

    def validate_issue(self, value):
        project_pk = self.context['view'].kwargs.get('project_pk')
        if not Issue.objects.filter(project_id=project_pk, id=value.id).exists():
            raise serializers.ValidationError()
        return value
