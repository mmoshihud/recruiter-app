from pty import CHILD
from rest_framework import serializers
from core.models import User
from messaging.choices import KindChoices
from messaging.models import Inbox, Message, Thread
from django.db.models import Q

from organization.models import Organization


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

        existing_inbox = Inbox.objects.filter(
            Q(user=sender, other_user=receiver) | Q(user=receiver, other_user=sender)
        ).first()

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
        fields = ["uid", "user", "other_user"]


class PrivateInboxMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["sender", "receiver", "content"]


class PrivateThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ["uid", "content"]

    def create(self, validated_data):
        sender = self.context["request"].user
        organization_uid = (
            self.context["request"].parser_context.get("kwargs").get("organization_uid")
        )
        try:
            organization = Organization.objects.get(uid=organization_uid)
        except Organization.DoesNotExist:
            raise serializers.ValidationError("Organization does not exist.")

        # Check if there is an existing thread for the sender and organization
        existing_thread = Thread.objects.filter(
            author=sender, organization=organization, kind=KindChoices.PARENT
        ).first()

        if existing_thread:
            # If an existing thread is found, add the message content to it
            print(existing_thread.parent)
            Thread.objects.create(
                parent=existing_thread.parent if existing_thread.parent else existing_thread,
                kind=KindChoices.CHILD,
                author=sender,
                organization=organization,
                **validated_data
            )
            return existing_thread
        else:
            # If no existing thread is found, create a new thread
            thread = Thread.objects.create(
                author=sender, organization=organization, **validated_data
            )
            return thread
