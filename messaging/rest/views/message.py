from messaging.models import Thread
from rest_framework import generics
from messaging.rest.serializers.message import (
    PrivatePrivateMessageListSerializer,
    PrivateThreadSerializer,
)


class PrivateThreadCreate(generics.CreateAPIView):
    serializer_class = PrivateThreadSerializer


class PrivateThreadDetail(generics.ListCreateAPIView):
    serializer_class = PrivatePrivateMessageListSerializer

    def get_queryset(self):
        thread_uid = self.kwargs["thread_uid"]
        thread = Thread.objects.get(uid=thread_uid)
        organization = thread.organization
        messages = Thread.objects.filter(organization=organization)
        return messages
