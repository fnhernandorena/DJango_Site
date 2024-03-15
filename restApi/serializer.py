from rest_framework import serializers
from .models import developer

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model=developer
        fields= "__all__"