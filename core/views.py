from rest_framework import generics
from core.models import OrganizationUser
from core.serializer import UserSerializer, OrganizationUserSerializer
from rest_framework.permissions import IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class OrganizationUserView(generics.CreateAPIView):
    serializer_class = OrganizationUserSerializer
    permission_classes = [IsAuthenticated]
