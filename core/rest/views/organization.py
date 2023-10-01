from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from organization.models import Organization
from core.rest.permission import IsSuperAdmin

from organization.rest.serializers.organization import (
    OrganizationListSerializer,
    OrganizationSerializer,
)


class PrivateOrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsSuperAdmin()]
        return [IsAuthenticated()]


class PrivateOrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer
    permission_classes = [IsSuperAdmin]

    def get_object(self):
        uid = self.kwargs.get("organization_uid")
        try:
            return Organization.objects.get(uid=uid)
        except Organization.DoesNotExist:
            raise ValidationError("Organization does not exist.")


class PrivateOrganizationOnboard(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsSuperAdmin]
