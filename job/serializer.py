from rest_framework import serializers
from core.models import User

from job.models import Application, Job, Offer


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = fields = ["name", "email", "resume_url"]

    def create(self, validated_data):
        job_id = self.context["view"].kwargs.get("pk")
        user = self.context["request"].user

        existing_application = Application.objects.filter(
            job_id=job_id, applicant=user
        ).first()
        if existing_application:
            raise serializers.ValidationError("You have already applied for this job.")

        name = validated_data.pop("name")
        email = validated_data.pop("email")
        resume_url = validated_data.pop("resume_url")

        application = Application(
            job_id=job_id,
            applicant=user,
            name=name,
            email=email,
            resume_url=resume_url,
        )
        application.save()
        return application


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"
