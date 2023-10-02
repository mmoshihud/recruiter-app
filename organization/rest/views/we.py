from rest_framework import generics
from core.rest.permission import IsOrganizationMember, IsOwnerAdminPermission
from organization.models import OrganizationUser


from organization.rest.serializers.organization import (
    OrganizationUserSerializer,
    OrganizationUserDetailSerializer,
)


class PrivateOrganizationUserList(generics.ListCreateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOwnerAdminPermission()]
        return [IsOrganizationMember()]


class PrivateOrganizationUserDetail(generics.RetrieveUpdateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserDetailSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsOrganizationMember()]
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return [IsOwnerAdminPermission()]
        return super().get_permissions()
