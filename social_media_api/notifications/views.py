from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get("pk")
        return generics.get_object_or_404(Post, pk=pk)  # ✅ Ensure this exists
