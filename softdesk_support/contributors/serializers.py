from rest_framework import serializers
from .models import Contributor
from users.models import CustomUser


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    project = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']
        read_only_fields = ['project']
