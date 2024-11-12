from rest_framework import serializers
from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'role']
