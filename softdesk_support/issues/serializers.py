from rest_framework import serializers
from .models import Issue
from contributors.models import Contributor

class IssueSerializer(serializers.ModelSerializer):
    # Ajouter liste de comments liés à l'issue?
    class Meta:
        model = Issue
        fields = ['id', 'author', 'project', 'title', 'description', 'assigned_to', 'priority', 'tag', 'status', 'created_time']
        read_only_fields = ['id', 'created_time', 'author', 'project']

    def validate_assigned_to(self, value):
        project = self.context['view'].kwargs.get('project_pk')
        if not Contributor.objects.filter(project_id=project, id=value.id).exists():
            raise serializers.ValidationError()
        return value
