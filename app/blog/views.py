from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost, Comment
from .serializers import PostSerializer, CommentSerializer, ThreadSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return BlogPost.objects.filter(
            user = self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return BlogPost.objects.filter(
            user = self.request.user
        )

class CommentList(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        
        return Comment.objects.filter(
            post_id=post_id, user=self.request.user, parent=None)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializer
        return ThreadSerializer


    def perform_create(self, serializer):
        post_id= self.request.query_params.get('post_id')
        parent_id= self.request.query_params.get('parent_id')


        post = get_object_or_404(BlogPost, pk=post_id)
        coment = None
        if parent_id:
            coment = get_object_or_404(Comment, pk=parent_id)
        
        serializer.save(user=self.request.user, parent=coment, post=post)
        



