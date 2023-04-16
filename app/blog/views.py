from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

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

