from rest_framework import generics
from core.rest.permission import IsOrganizationMember, IsOwnerAdminPermission
from messaging.choices import KindChoices
from messaging.models import Thread
from organization.models import Organization, OrganizationUser

from organization.rest.serializers.organization import (
    PrivateMessageList,
    PrivateMessageThreadList,
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


class PrivatePrivateMessageList(generics.ListCreateAPIView):
    serializer_class = PrivateMessageThreadList  # list serializer == message cross

    def get_queryset(self):
        user = self.request.user
        organization = Organization.objects.filter(organizationuser__user=user).first()
        threads = Thread.objects.filter(
            organization=organization, kind=KindChoices.PARENT
        )
        return threads

    # perform create or serializer create


class PrivateMessageDetail(generics.ListCreateAPIView):  # ok
    serializer_class = PrivateMessageList  # detail serializer

    def get_queryset(self):
        thread_uid = self.kwargs["thread_uid"]
        thread = Thread.objects.get(uid=thread_uid)  # try catch
        author = thread.author
        organization = thread.organization
        messages = Thread.objects.filter(author=author) | Thread.objects.filter(
            organization=organization
        )
        return messages


# class PrivateChildOrganizationList(generics.ListCreateAPIView):
#     serializer_class = OrganizationChildSerializer

#     def get_queryset(self):
#         user = self.context["request"].user
#         organization = Organization.objects.filter(organizationuser__user=user).first()
#         if organization:
#             # Filter the queryset to only show child organizations for the current organization.
#             return Organization.objects.filter(parent_organization_id=organization)
#         else:
#             # If no parent_org_id is provided, return all organizations.
#             return None
