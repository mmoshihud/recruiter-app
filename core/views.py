from django.shortcuts import render
from rest_framework import generics
from core.models import OrganizationUser
from core.serializer import UserSerializer, OrganizationUserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class OrganizationUserView(generics.CreateAPIView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer
