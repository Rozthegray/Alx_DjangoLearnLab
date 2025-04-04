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
        # Use get_object_or_404 to get the post by pk
        post = get_object_or_404(Post, pk=pk)

        # Create or retrieve the Like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification when a post is liked
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
                timestamp=timezone.now()
            )

        return Response({"detail": "Post liked successfully."}, status=201)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to get the post by pk
        post = get_object_or_404(Post, pk=pk)

        # Check if the Like object exists, then delete it
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=200)
        else:
            return Response({"
