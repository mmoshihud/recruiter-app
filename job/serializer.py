from rest_framework import serializers
from core.models import User
from core.serializer import UserSerializer

from job.models import Application, Feedback, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = fields = ["user_data", "name", "email", "resume_url"]

    def create(self, validated_data):
        job_id = self.context["view"].kwargs.get("job_id")
        user = self.context["request"].user

        existing_application = Application.objects.filter(
            job_id=job_id, applicant=user
        ).first()
        if existing_application:
            raise serializers.ValidationError("You have already applied for this job.")

        application = Application.objects.create(
            job_id=job_id, applicant=user, **validated_data
        )
        return application

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_data = UserSerializer(instance.applicant).data
        data["user_data"] = user_data
        return data


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["feedback_description", "feedback_rating"]

    def create(self, validated_data):
        application_id = self.context["view"].kwargs.get("app_id")
        feedback = Feedback.objects.create(
            application_id=application_id, **validated_data
        )
        return feedback

    def validate(self, data):
        application_id = self.context["view"].kwargs.get("app_id")
        try:
            application = Application.objects.get(id=application_id)
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
