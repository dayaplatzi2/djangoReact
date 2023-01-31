from rest_framework import serializers
from .models import Tutorial, Todo

'''class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo'''

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'published',
        )
        model = Tutorial
