from .models import BlogPost, Comment
from rest_framework import serializers
from user.serializers import UserSerializer
from django.shortcuts import get_object_or_404

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'user')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'body', 'parent', 'post', 'created_at')
        read_only_fields = ('parent', 'post', )
    

class ThreadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    children = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('id', 'user', 'body', 'parent', 'post', 'created_at', 'children')
        read_only_fields = ('parent', 'post', )

    def get_children(self, obj):
        sub_comments = Comment.objects.filter( parent=obj.id)
        return CommentSerializer(sub_comments, many=True).data
        
