from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from accounts.models import CustomUser  # Import CustomUser model

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the list of users the current user follows
        following_users = request.user.following.all()

        # Retrieve posts from followed users, ordered by creation date (newest first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts (assuming you have a PostSerializer)
        from .serializers import PostSerializer
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)
