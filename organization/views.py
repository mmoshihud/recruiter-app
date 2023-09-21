from rest_framework import generics
from core.permission import IsOrganizationMember, IsOwnerAdminPermission
from organization.models import OrganizationUser

from organization.serializer import OrganizationUserSerializer


class OrganizationUserCreateView(generics.ListCreateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer
    permission_classes = [IsOwnerAdminPermission]


class OrganizationUserDetailView(generics.RetrieveAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer
    permission_classes = [IsOrganizationMember]
