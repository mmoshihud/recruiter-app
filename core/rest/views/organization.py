from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from organization.models import Organization
from core.rest.permission import IsSuperAdmin

from organization.rest.serializers.organization import (
    OrganizationSerializer,
    OrganizationCreateSerializer,
)


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsSuperAdmin()]
        return [IsAuthenticated()]


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer
    permission_classes = [IsSuperAdmin]

    def get_object(self):
        uid = self.kwargs.get("organization_uid")
        object = self.queryset.get(uid=uid)
        return object


class OrganizationOnboardView(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsSuperAdmin]
