from rest_framework import serializers

from .models import Project
from contributors.models import Contributor
from contributors.serializers import ContributorSerializer


class ProjectListSerializer(serializers.ModelSerializer):
    """Serializer to display basics informations about a project."""

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'created_time']
        read_only_fields = ['created_time']


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Serializer to display complete informations about a project."""
    author = serializers.StringRelatedField()
    contributors = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'author', 'name', 'description', 'type', 'created_time', 'contributors']
        read_only_fields = ['author', 'created_time']

    def get_contributors(self, obj):
        contributors = Contributor.objects.filter(project=obj)
        return ContributorSerializer(contributors, many=True).data
