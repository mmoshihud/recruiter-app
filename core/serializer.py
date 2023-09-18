from urllib import request
from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import OrganizationUser, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class OrganizationUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = OrganizationUser
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user, _ = User.objects.get_or_create(
            email=user_data["email"], defaults=user_data
        )
        request = self.context.get("request")
        user = request.user
        organization_user = OrganizationUser.objects.create(user=user, **validated_data)
        return organization_user
