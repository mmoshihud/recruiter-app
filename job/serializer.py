from rest_framework import serializers
from core.serializer import UserSerializer

from job.models import Application, Feedback, Job
import uuid

from organization.models import Organization, OrganizationUser
from organization.serializer import OrganizationSerializer


class JobSerializer(serializers.ModelSerializer):
    job_poster = UserSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            "uuid",
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


class ApplicationSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            "uuid",
            "name",
            "email",
            "resume_url",
            "user_data",
            "application_date",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        job_uuid = self.context["request"].parser_context.get("kwargs").get("job_uuid")
        user = self.context["request"].user

        existing_application = Application.objects.filter(
            job__uuid=job_uuid, applicant=user
        ).first()
        if existing_application:
            raise serializers.ValidationError("You have already applied for this job.")

        try:
            job = Job.objects.get(uuid=job_uuid)
        except Job.DoesNotExist:
            raise serializers.ValidationError("Job does not exist.")

        application = Application.objects.create(
            job=job, applicant=user, **validated_data
        )
        return application

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_data = UserSerializer(instance.applicant).data
        data["user_data"] = user_data
        return data


class JobApplicationSerializer(serializers.ModelSerializer):
    data = "data"


class FeedbackSerializer(serializers.ModelSerializer):
    application_data = ApplicationSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "uuid",
            "application",
            "feedback_description",
            "feedback_rating",
            "created_at",
            "updated_at",
            "application_data",
        ]

    def create(self, validated_data):
        application_uuid = (
            self.context["request"].parser_context.get("kwargs").get("application_uuid")
        )
        application = Application.objects.get(uuid=application_uuid)
        feedback = Feedback.objects.create(application=application, **validated_data)
        return feedback

    def validate(self, data):
        print(self.context["request"].parser_context)

        application_uuid = (
            self.context["request"].parser_context.get("kwargs").get("application_uuid")
        )

        try:
            application = Application.objects.get(uuid=application_uuid)
            print("app", application)
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
