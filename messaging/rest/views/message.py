from messaging.models import Thread
from rest_framework import generics
from messaging.choices import KindChoices
from messaging.rest.serializers.message import (
    PrivatePrivateMessageListSerializer,
    PrivateThreadSerializer,
    PrivateThreadListSerializer,
)


class PrivateThreadCreate(generics.CreateAPIView):
    serializer_class = PrivateThreadSerializer


class PrivateThreadList(generics.ListAPIView):
    serializer_class = PrivateThreadListSerializer

    def get_queryset(self):
        user = self.request.user
        threads = Thread.objects.filter(author=user)
        last_message = threads.first()
        return [last_message] if last_message else []


class PrivateThreadDetail(generics.ListAPIView):
    serializer_class = PrivatePrivateMessageListSerializer

    def get_queryset(self):
        thread_uid = self.kwargs["thread_uid"]
        thread = Thread.objects.get(uid=thread_uid)
        organization = thread.organization
        messages = Thread.objects.filter(organization=organization)
        return messages
