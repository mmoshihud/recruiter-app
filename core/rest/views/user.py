from rest_framework import generics
from core.models import User
from core.rest.permission import IsSuperAdmin
from core.rest.serializers.user import UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class PublicUserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class PrivateUserList(generics.ListAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = [IsSuperAdmin]


class PrivateUserProfileUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
