from rest_framework import serializers
from core.models import User

from core.rest.serializers.user import UserSerializer
from organization.choices import RoleChoices
from organization.models import Organization, OrganizationUser


class OrganizationSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    role = serializers.ChoiceField(choices=RoleChoices.choices, write_only=True)

    class Meta:
        model = Organization
        fields = [
            "uid",
            "name",
            "email",
            "phone",
            "description",
            "location",
            "status",
            "created_at",
            "updated_at",
            "user",
            "role",
        ]

    def create(self, validated_data):
        role = validated_data.pop("role")
        user_data = validated_data.pop("user")
        organization = Organization.objects.create(**validated_data)
        user = User.objects.create_user(**user_data)
        OrganizationUser.objects.create(user=user, organization=organization, role=role)
        return organization


class OrganizationUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    organization = OrganizationSerializer(required=False, read_only=True)

    class Meta:
        model = OrganizationUser
        fields = ["uid", "role", "user", "organization"]

    def create(self, validated_data):
        user = self.context["request"].user
        organization = Organization.objects.filter(organizationuser__user=user).first()
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        organization_user = OrganizationUser.objects.create(
            user=user, organization=organization, **validated_data
        )
        return organization_user


class OrganizationUserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False, read_only=True)
    organization = OrganizationSerializer(required=False, read_only=True)

    class Meta:
        model = OrganizationUser
        fields = ["user", "role", "organization"]

    def update(self, instance, validated_data):
        instance.role = validated_data["role"]
        instance.save()
        return instance


class OrganizationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "uid",
            "name",
            "email",
            "phone",
            "description",
            "location",
            "status",
            "created_at",
            "updated_at",
        ]