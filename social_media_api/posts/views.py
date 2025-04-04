# posts/views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated permission
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# Apply permissions to ensure user is authenticated
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def like_post(request, pk):
    # Use get_object_or_404 to retrieve the post object
    post = get_object_or_404(Post, pk=pk)

    # Prevent liking a post multiple times
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create notification for the post's author
    recipient = post.user  # The user who created the post
    verb = f"liked your post: {post.content[:20]}..."  # Notification verb

    # Create a notification instance
    notification = Notification.objects.create(
        recipient=recipient,
        actor=request.user,
        verb=verb,
        target_ct=ContentType.objects.get_for_model(post),
        target_id=post.id
    )

    return Response({"detail": "Post liked and notification sent."}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def unlike_post(request, pk):
    # Use get_object_or_404 to retrieve the post object
    post = get_object_or_404(Post, pk=pk)

    # Prevent unliking a post that wasn't liked
    like = Like.objects.filter(user=request.user, post=post).first()

    if not like:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()  # Delete the like

    return Response({"detail": "Post unliked."
