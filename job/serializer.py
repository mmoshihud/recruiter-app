from rest_framework import serializers
from core.models import User

from job.models import Application, Feedback, Job, Offer


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = fields = ["name", "email", "resume_url"]

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


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["feedback_description", "feedback_rating"]

    def create(self, validated_data):
        application_id = self.context["view"].kwargs.get("feed_id")
        feedback = Feedback.objects.create(
            application_id=application_id, **validated_data
        )
        return feedback

    def validate(self, data):
        # Get the application for which feedback is being created
        application_id = self.context["view"].kwargs.get("feed_id")
        application = self.get_application(application_id)

        # Check if feedback already exists for the same applicant and application
        existing_feedback = Feedback.objects.filter(
            application=application,
            application__applicant=application.applicant,
        ).first()

        if existing_feedback:
            raise serializers.ValidationError(
                "Feedback for this application by the same applicant already exists."
            )

        return data

    def get_application(self, application_id):
        try:
            return Application.objects.get(id=application_id)
        except Application.DoesNotExist:
            raise serializers.ValidationError(
                "Application with this ID does not exist."
            )
