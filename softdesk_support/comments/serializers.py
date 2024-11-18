from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Comment
from issues.models import Issue


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    issue_url = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'issue', 'issue_url', 'description', 'created_time']
        read_only_fields = ['id', 'author', 'issue', 'issue_url', 'created_time']

    def get_issue_url(self, obj):
        request = self.context.get('request')
        if obj.issue:
            return reverse(
                'issues-detail',
                kwargs={
                    'project_pk': obj.issue.project.id,
                    'pk': obj.issue.id
                },
                request=request
            )
        return None

    def validate_issue(self, value):
        project_pk = self.context['view'].kwargs.get('project_pk')
        if not Issue.objects.filter(project_id=project_pk, id=value.id).exists():
            raise serializers.ValidationError()
        return value
