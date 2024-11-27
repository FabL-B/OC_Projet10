from rest_framework import serializers
from .models import Issue
from contributors.models import Contributor


class IssueSerializer(serializers.ModelSerializer):
    """
    Serializer for the Issue model.
    """
    author = serializers.StringRelatedField()
    class Meta:
        model = Issue
        fields = [
            'id',
            'author',
            'project',
            'title',
            'description',
            'assigned_to',
            'priority',
            'tag',
            'status',
            'created_time'
        ]
        read_only_fields = ['id', 'created_time', 'author', 'project']

    def validate_assigned_to(self, value):
        """Validate that the assigned contributor is part of the project."""
        project = self.context['view'].kwargs.get('project_pk')
        if not Contributor.objects.filter(project_id=project, id=value.id).exists():
            raise serializers.ValidationError(
                "The assigned contributor does not belong to the project."
            )
        return value

class IssueListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing issues.
    """
    author = serializers.StringRelatedField()
    class Meta:
        model = Issue
        fields = ['id', 'author', 'project', 'assigned_to', 'title']
        read_only_fields = fields
