from rest_framework.schemas.coreapi import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'name',
            'created_at',
            'done',
            'user'
        ]
