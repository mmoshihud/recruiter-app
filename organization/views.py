from rest_framework import generics
from core.permission import IsOrganizationMember, IsOwnerAdminPermission
from organization.models import OrganizationUser

from organization.serializer import (
    OrganizationUserSerializer,
    OrganizationUserUpdateSerializer,
)


class OrganizationUserCreateView(generics.ListCreateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOwnerAdminPermission()]
        return [IsOrganizationMember()]


class OrganizationUserDetailView(generics.RetrieveUpdateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserUpdateSerializer
    permission_classes = [IsOwnerAdminPermission]
