from rest_framework import serializers
from core.models import User
from core.serializer import UserSerializer

from job.models import Application, Feedback, Job
import uuid


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = "__all__"

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


class FeedbackSerializer(serializers.ModelSerializer):
    application_data = ApplicationSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ["feedback_description", "feedback_rating", "application_data"]
        # fields = "__all__"

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
