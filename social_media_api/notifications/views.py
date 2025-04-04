# notifications/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from notifications.models import Notification
from django.utils import timezone

class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get notifications for the authenticated user
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')

        # Serialize notifications data
        notification_data = [
            {
                "id": notification.id,
                "actor": notification.actor.username,  # or use a field like notification.actor.get_full_name()
                "verb": notification.verb,
                "target": str(notification.target),  # You can adjust this as needed, or serialize the target
                "timestamp": notification.timestamp,
                "read": notification.read  # Assuming you have a 'read' field
            }
            for notification in notifications
        ]

        return Response(notification_data)

class NotificationReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the notification
        notification = Notification.objects.filter(id=pk, recipient=request.user).first()
        
        if not notification:
            return Response({"detail": "Notification not found or not authorized to view this notification."}, status=404)
        
        # Mark the notification as read
        notification.read = True
        notification.save()

        return Response({"detail": "Notification marked as read."})

class NotificationUnreadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Retrieve the notification
        notification = Notification.objects.filter(id=pk, recipient=request.user).first()
        
        if not notification:
            return Response({"detail": "Notification not found or not authorized to view this notification."}, status=404)
        
        # Mark the notification as unread
        notification.read = False
        notification.save()

        return Response({"detail": "Notification marked as unread."})
