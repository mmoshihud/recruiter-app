from django.shortcuts import get_object_or_404
from rest_framework import generics
from core.rest.permission import IsOrganizationMember, IsOwnerAdminPermission
from messaging.choices import KindChoices
from messaging.models import Thread
from organization.models import Organization, OrganizationUser


from organization.rest.serializers.organization import (
    MessageList,
    MessageThreadList,
    OrganizationChildSerializer,
    OrganizationUserSerializer,
    OrganizationUserDetailSerializer,
)


class PrivateOrganizationUserList(generics.ListCreateAPIView):
    queryset = OrganizationUser.objects.filter()
    serializer_class = OrganizationUserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOwnerAdminPermission()]
        return [IsOrganizationMember()]


class PrivateOrganizationUserDetail(generics.RetrieveUpdateAPIView):
    queryset = OrganizationUser.objects.filter()
    serializer_class = OrganizationUserDetailSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsOrganizationMember()]
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return [IsOwnerAdminPermission()]
        return super().get_permissions()


class PrivateChildOrganizationList(generics.CreateAPIView):
    serializer_class = OrganizationChildSerializer


class PrivateMessageList(generics.ListAPIView):
    serializer_class = MessageThreadList

    def get_queryset(self):
        user = self.request.user
        organization = Organization.objects.filter(organizationuser__user=user).first()
        threads = Thread.objects.filter(
            organization=organization, kind=KindChoices.PARENT
        )
        return threads


class PrivateMessageDetail(generics.ListCreateAPIView):
    serializer_class = MessageList

    def get_queryset(self):
        thread_uid = self.kwargs["uid"]
        thread = Thread.objects.get(uid=thread_uid)
        author = thread.author
        messages = Thread.objects.filter(author=author)
        return messages
