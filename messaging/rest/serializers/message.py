from rest_framework import serializers
from core.models import User
from messaging.models import Inbox, Message


class MessageSerializer(serializers.ModelSerializer):
    receiver_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Message
        fields = ["content", "receiver_email"]

    def create(self, validated_data):
        sender = self.context["request"].user

        receiver_email = validated_data.get("receiver_email")
        try:
            receiver = User.objects.get(email=receiver_email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"receiver_email": "Receiver with this email does not exist."}
            )

        existing_inbox = Inbox.objects.filter(user=sender, other_user=receiver).first()

        if existing_inbox:
            inbox = existing_inbox
        else:
            inbox = Inbox.objects.create(user=sender, other_user=receiver)

        content = validated_data.get("content")

        message = Message.objects.create(
            inbox=inbox, sender=sender, receiver=receiver, content=content
        )

        return message


class PrivateInboxListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = "__all__"


class PrivateInboxMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
