# posts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from posts.models import Post, Like
from notifications.models import Notification
from django.utils import timezone

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Fetch the post object, or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        # Get or create the Like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        # If the like was created, also create a notification
        if created:
            # Create a notification for the post author that their post was liked
            notification = Notification.objects.create(
                recipient=post.author,  # Assuming the post author should be notified
                actor=request.user,  # The user who liked the post
                verb="liked your post",
                target=post,  # Targeting the post
                timestamp=timezone.now()
            )

        return Response({"detail": "Post liked successfully."}, status=201)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Fetch the post object, or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        # Try to retrieve the like object for the current user and post
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            # If a like exists, delete it
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=200)
        else:
            return Response({"detail": "Like not found."}, status=404)
