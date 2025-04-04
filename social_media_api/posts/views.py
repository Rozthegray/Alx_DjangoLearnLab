# Importing necessary modules
from django.shortcuts import get_object_or_404  # <-- Add this line
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.utils import timezone

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the post or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post
        if Like.objects.filter(post=post, user=request.user).exists():
            return Response({"detail": "You already liked this post."}, status=400)

        # Create a new Like record
        Like.objects.create(post=post, user=request.user)

        # Optionally, create a notification
        Notification.objects.create(
            recipient=post.author,  # The author of the post
            actor=request.user,  # The user who liked the post
            verb="liked",  # Describes the action
            target=post,  # The post that was liked
            timestamp=timezone.now()
        )

        return Response({"detail": "Post liked successfully."}, status=200)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the post or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        like = Like.objects.filter(post=post, user=request.user).first()
        if not like:
            return Response({"detail": "You haven't liked this post."}, status=400)

        # Delete the Like record (unliking the post)
        like.delete()

        # Optionally, create a notification for unliking
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="unliked",
            target=post,
            timestamp=timezone.now()
        )

        return Response({"detail": "Post unliked successfully."}, status=200)
