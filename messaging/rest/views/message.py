from django.shortcuts import get_object_or_404
from rest_framework import generics
from messaging.models import Inbox, Message
from messaging.rest.serializers.message import (
    MessageSerializer,
    PrivateInboxListSerializer,
    PrivateInboxMessageSerializer,
    PrivateThreadSerializer,
)
from rest_framework.validators import ValidationError


class PrivateMessageCreate(generics.CreateAPIView):
    serializer_class = MessageSerializer


class PrivateInboxList(generics.ListAPIView):
    serializer_class = PrivateInboxListSerializer

    def get_queryset(self):
        user = self.request.user
        return Inbox.objects.filter(user=user) | Inbox.objects.filter(other_user=user)


class PrivateMessageDetail(generics.ListAPIView):
    serializer_class = PrivateInboxMessageSerializer

    def get_queryset(self):
        inbox_uid = self.kwargs["inbox_uid"]
        user = self.request.user

        inbox = get_object_or_404(Inbox, uid=inbox_uid)

        if user != inbox.user and user != inbox.other_user:
            raise ValidationError("You do not have permission to access this inbox.")

        return Message.objects.filter(
            inbox=inbox, sender=user
        ) | Message.objects.filter(inbox=inbox, receiver=user)


class PrivateThreadCreate(generics.CreateAPIView):
    serializer_class = PrivateThreadSerializer
