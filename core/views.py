from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from organization.models import Organization
from core.permission import IsSuperAdmin
from core.serializer import UserSerializer
from organization.serializer import OrganizationSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsSuperAdmin()]
        return [IsAuthenticated()]


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsSuperAdmin]

    def get_object(self):
        uuid = self.kwargs.get("organization_uuid")
        object = self.queryset.get(uuid=uuid)
        return object


class OrganizationOnboardView(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsSuperAdmin]
