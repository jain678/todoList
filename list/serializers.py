from rest_framework import serializers
from .models import Tasks
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'date', 'is_completed']