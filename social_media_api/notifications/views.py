from django.shortcuts import get_object_or_404  # Add this import
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get("pk")  # Get the post ID from URL parameters
        return get_object_or_404(Post, pk=pk)  # Use get_object_or_404
