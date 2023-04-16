from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions', )
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login', 'email')
