from rest_framework import generics
from core.models import User
from notification.models import Notification
from notification.rest.serializer.notification import NotificationSerializer
from organization.models import OrganizationUser


class PrivateNotificationList(generics.ListAPIView):
    # queryset = Notification.objects.filter(is_read=False)
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        # queryset = User.objects.filter()
        # queryset = queryset.exclude(organizationuser__user=user)
        queryset = Notification.objects.filter(organization=None)
        queryset = queryset.exclude(organization__organizationuser__user=user)
        # notification = Notification.objects.filter(is_read=False)
        return queryset
