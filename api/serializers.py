from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'execution_period', 'executed')


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'execution_period')


class TaskExecutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'executed')
