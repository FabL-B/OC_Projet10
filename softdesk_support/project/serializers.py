from rest_framework import serializers
from .models import Project, Contributor, Issue, Comments


class ContributorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = ['id', 'user']


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'author', 'name', 'description', 'type', 'created_time',]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'author', 'project', 'title', 'description', 'assigned_to', 'priority', 'tag', 'status', 'created_time']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'author', 'issue', 'description', 'created_time']
