from django.contrib.auth import get_user_model

from rest_framework import serializers

from organization.models import OrganizationUser
from drf_spectacular.utils import extend_schema_field

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    has_organization = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["uid", "name", "email", "password", "phone", "has_organization"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 6}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    @extend_schema_field(bool)
    def get_has_organization(self, obj):
        return OrganizationUser.objects.filter(user=obj).exists()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["uid", "name", "email", "password", "phone"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 6}}

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        return super().update(instance, validated_data)
