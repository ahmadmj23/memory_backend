from rest_framework import serializers
from .models import Artifact

class ArtifactSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Artifact
        fields = [
            'id', 'title', 'description', 'era', 'type', 
            'file', 'status', 'owner', 'owner_username', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['status', 'owner', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Assign owner from context
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)
