from rest_framework import generics
from core.rest.permission import IsOrganizationMember, IsOwnerAdminPermission
from organization.models import OrganizationUser

from organization.rest.serializers import (
    OrganizationUserSerializer,
    OrganizationUserUpdateSerializer,
)


class OrganizationUserListCreateView(generics.ListCreateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOwnerAdminPermission()]
        return [IsOrganizationMember()]


class OrganizationUserDetailView(generics.RetrieveUpdateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserUpdateSerializer
    lookup_field = "uuid"

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsOrganizationMember()]
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return [IsOwnerAdminPermission()]
        return super().get_permissions()
