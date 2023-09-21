from rest_framework import serializers

from core.models import User
from core.serializer import UserSerializer
from job.serializer import JobSerializer
from organization.models import OrganizationUser, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    organization = OrganizationSerializer(required=False)

    class Meta:
        model = OrganizationUser
        fields = ["user", "role", "organization"]

    def create(self, validated_data):
        user = self.context["request"].user
        organization = Organization.objects.filter(organizationuser__user=user).first()
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        organization_user = OrganizationUser.objects.create(
            user=user, organization=organization, **validated_data
        )
        return organization_user
