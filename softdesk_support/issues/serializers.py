from rest_framework import serializers
from .models import Issue
from contributors.models import Contributor

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'assigned_to', 'priority', 'tag', 'status', 'created_time']
        read_only_fields = ['id', 'created_time']

    def validate_assigned_to(self, value):
        project = self.context['project']
        if not Contributor.objects.filter(project=project, user=value.user).exists():
            raise serializers.ValidationError()
        return value