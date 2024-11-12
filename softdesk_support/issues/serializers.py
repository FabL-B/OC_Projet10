from rest_framework import serializers

from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'author', 'project', 'title', 'description', 'assigned_to', 'priority', 'tag', 'status', 'created_time']
