from rest_framework import generics
from notification.models import Notification
from notification.rest.serializer.notification import NotificationSerializer


class PrivateNotificationList(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Notification.objects.filter(organization=None)
        notification = queryset.exclude(organization__organizationuser__user=user)
        return notification
