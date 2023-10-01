from rest_framework import serializers
from core.rest.serializers.user import UserSerializer

from job.models import Application, Feedback, Job
from me.rest.serializers.application import ApplicationSerializer
from organization.models import Organization
from organization.rest.serializers.organization import OrganizationSerializer


class JobSerializer(serializers.ModelSerializer):
    job_poster = UserSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            "uid",
            "title",
            "vacancy",
            "location",
            "description",
            "requirements",
            "salary",
            "posting_date",
            "expiration_date",
            "job_poster",
            "organization",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        organization = Organization.objects.filter(organizationuser__user=user).first()

        if not organization:
            raise serializers.ValidationError(
                "User is not associated with any organization."
            )

        validated_data["organization"] = organization
        validated_data["job_poster"] = user

        job = Job.objects.create(**validated_data)
        return job


class FeedbackSerializer(serializers.ModelSerializer):
    application_data = ApplicationSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "uid",
            "feedback_description",
            "feedback_rating",
            "created_at",
            "updated_at",
            "application_data",
        ]

    def create(self, validated_data):
        application_uid = (
            self.context["request"].parser_context.get("kwargs").get("application_uid")
        )
        application = Application.objects.get(uid=application_uid)
        feedback = Feedback.objects.create(application=application, **validated_data)
        return feedback

    def validate(self, data):
        application_uid = (
            self.context["request"].parser_context.get("kwargs").get("application_uid")
        )

        try:
            application = Application.objects.get(uid=application_uid)
        except Application.DoesNotExist:
            raise serializers.ValidationError(
                "Application with this ID does not exist."
            )

        existing_feedback = Feedback.objects.filter(
            application=application,
            application__applicant=application.applicant,
        ).first()

        if existing_feedback:
            raise serializers.ValidationError(
                "Feedback for this application by the same applicant already exists."
            )

        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        application_data = ApplicationSerializer(instance.application).data
        data["application_data"] = application_data
        return data
