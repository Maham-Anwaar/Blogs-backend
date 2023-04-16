from .models import BlogPost
from rest_framework import serializers
from user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'user')
