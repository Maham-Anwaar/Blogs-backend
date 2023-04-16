from user import models, serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return get_object_or_404(models.User, id=self.request.user.id)
