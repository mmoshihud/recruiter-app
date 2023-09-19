from rest_framework import generics
from core.models import Organization
from core.serializer import (
    OrganizationSerializer,
    UserSerializer,
    OrganizationUserSerializer,
)
from rest_framework.permissions import IsAuthenticated


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class OrganizationUserView(generics.CreateAPIView):
    serializer_class = OrganizationUserSerializer
    permission_classes = [IsAuthenticated]


class OrganizationCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
