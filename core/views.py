from rest_framework import generics

from organization.models import Organization
from core.permission import IsSuperAdmin
from core.serializer import UserSerializer
from organization.serializer import OrganizationSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsSuperAdmin]


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsSuperAdmin]
