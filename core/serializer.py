from django.contrib.auth import get_user_model

from rest_framework import serializers

from core.models import Organization, OrganizationUser, User


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
        fields = ["user", "role", "organization"]
        extra_kwargs = {"organization": {"required": False}}

    def create(self, validated_data):
        user = self.context["request"].user
        organization = Organization.objects.filter(organizationuser__user=user).first()
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        organization_user = OrganizationUser.objects.create(
            user=user, organization=organization, **validated_data
        )
        return organization_user


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
