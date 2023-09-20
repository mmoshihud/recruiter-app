from rest_framework import generics
from core.models import Organization
from core.serializer import (
    OrganizationSerializer,
    UserSerializer,
    OrganizationUserSerializer,
)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class OrganizationUserCreateView(generics.CreateAPIView):
    serializer_class = OrganizationUserSerializer


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
