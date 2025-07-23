from rest_framework import serializers
from .models import User

# serializer converts user model to/from JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields user can see or get back
        fields = [
            'id',
            'email',
            'username',
            'bio',
            'avatar',
            'credits',
            'created_at',
        ]
        # fields that aren't editable via API
        read_only_fields = ['id', 'credits', 'created_at']
