from rest_framework.schemas.coreapi import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'done', 'created_at', 'user']
