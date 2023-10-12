from rest_framework import serializers

from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    unread_count = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = "__all__"

    def get_unread_count(self, obj):
        return Notification.objects.filter(
            is_read=True, organization=obj.organization
        ).count()
