from rest_framework import serializers
from messaging.choices import KindChoices
from messaging.models import Thread

from organization.models import Organization


class PrivateThreadSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    organization = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = ["uid", "kind", "author", "content", "organization", "is_read"]
        read_only_fields = ["author", "organization"]

    def create(self, validated_data):
        sender = self.context["request"].user
        organization_uid = (
            self.context["request"].parser_context.get("kwargs").get("organization_uid")
        )
        try:
            organization = Organization.objects.get(uid=organization_uid)
        except Organization.DoesNotExist:
            raise serializers.ValidationError("Organization does not exist.")

        # Check if there is an existing thread for the sender and organization
        existing_thread = Thread.objects.filter(
            author=sender, organization=organization, kind=KindChoices.PARENT
        ).first()

        if existing_thread:
            # If an existing thread is found, add the message content to it
            thread = Thread.objects.create(
                parent=existing_thread.parent
                if existing_thread.parent
                else existing_thread,
                kind=KindChoices.CHILD,
                author=sender,
                organization=organization,
                **validated_data
            )
            return thread
        else:
            # If no existing thread is found, create a new thread
            thread = Thread.objects.create(
                author=sender, organization=organization, **validated_data
            )
            return thread

    def get_author(self, obj):
        return obj.author.name

    def get_organization(self, obj):
        return obj.organization.name


class PrivateThreadListSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = ["organization", "content", "is_read", "created_at"]

    def get_organization(self, obj):
        return obj.organization.name


class PrivatePrivateMessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ["content", "is_read", "created_at"]
