from rest_framework import serializers

from .models import Project
from contributors.models import Contributor
from contributors.serializers import ContributorSerializer


class ProjectListSerializer(serializers.ModelSerializer):
    """
    Serializer to display basic information about a project.

    Includes the project's ID, name, description, type, and creation date.
    """

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'type',
            'created_time'
        ]
        read_only_fields = ['created_time']


class ProjectDetailSerializer(serializers.ModelSerializer):
    """
    Serializer to display detailed information about a project.

    Includes additional fields like the author's name and the list of
    contributors to the project.
    """
    author = serializers.StringRelatedField()
    contributors = serializers.SerializerMethodField()

    class Meta:
        """Retrieve and serialize the list of contributors for the project."""
        model = Project
        fields = [
            'id',
            'author',
            'name',
            'description',
            'type',
            'created_time',
            'contributors'
        ]
        read_only_fields = ['author', 'created_time']

    def get_contributors(self, obj):
        contributors = Contributor.objects.filter(project=obj)
        return ContributorSerializer(contributors, many=True).data
