from django.db import models
from user.models import User
from uuid import uuid4

class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s")
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="%(class)s")
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,  related_name="%(class)s")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,  related_name="%(class)s")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.post}"
