from core.rest.serializers.user import UserSerializer
from job.models import Application, Job
from rest_framework import serializers


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
            "status",
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
