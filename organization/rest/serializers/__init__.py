from rest_framework import serializers
from core.rest.serializers import UserSerializer

from core.models import User
from job.models import Application, Feedback, Job
from organization.models import Organization, OrganizationUser


class OrganizationSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    role = serializers.CharField(write_only=True)

    class Meta:
        model = Organization
        fields = [
            "uid",
            "name",
            "email",
            "phone",
            "description",
            "location",
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


class OrganizationUserUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False, read_only=True)
    organization = OrganizationSerializer(required=False, read_only=True)

    class Meta:
        model = OrganizationUser
        fields = ["user", "role", "organization"]

    def update(self, instance, validated_data):
        instance.role = validated_data["role"]
        instance.save()
        return instance


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


class ApplicationSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            "uid",
            "name",
            "email",
            "resume_url",
            "user_data",
            "application_date",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        job_uid = self.context["request"].parser_context.get("kwargs").get("job_uid")
        user = self.context["request"].user

        existing_application = Application.objects.filter(
            job__uid=job_uid, applicant=user
        ).first()
        if existing_application:
            raise serializers.ValidationError("You have already applied for this job.")

        try:
            job = Job.objects.get(uid=job_uid)
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
            "uid",
            "application",
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


class OrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "uid",
            "name",
            "email",
            "phone",
            "description",
            "location",
            "created_at",
            "updated_at",
        ]
