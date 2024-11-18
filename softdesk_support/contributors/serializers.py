from rest_framework import serializers
from .models import Contributor
from users.models import CustomUser


class ContributorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contributor model.

    Serializes the relationship between a user and a project,
    including the contributor's role.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    project = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']
        read_only_fields = ['project']
