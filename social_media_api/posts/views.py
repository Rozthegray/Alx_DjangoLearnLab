from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404  # Corrected import
from posts.models import Post, Like
from notifications.models import Notification
from django.utils import timezone

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Correct usage of get_object_or_404 to fetch the Post object
        post = get_object_or_404(Post, pk=pk)

        # Create or get the Like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        # If the like is created, also create a notification
        if created:
            notification = Notification.objects.create(
                recipient=post.author,  # Assuming the post author should be notified
                actor=request.user,  # The user who liked the post
                verb="liked your post",
                target=post,  # The target is the post that was liked
                timestamp=timezone.now()
            )

        return Response({"detail": "Post liked successfully."}, status=201)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Correct usage of get_object_or_404 to fetch the Post object
        post = get_object_or_404(Post, pk=pk)

        # Try to retrieve the Like object for the current user and post
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            # If a like exists, delete it
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=200)
        else:
            return Response({"detail": "Like not found."}, status=404)
