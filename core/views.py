from django.shortcuts import render
from rest_framework import generics
from core.serializer import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
