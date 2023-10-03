from rest_framework import serializers

from job.models import FavoriteList, Job
from organization.rest.serializers.job import JobListSerializer, JobSerializer


class PrivateFavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = [
            "uid",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        job_uid = self.context["request"].parser_context.get("kwargs").get("job_uid")

        job = Job.objects.get(uid=job_uid)

        applicant = self.context["request"].user

        favorite_list = FavoriteList.objects.create(
            job=job, applicant=applicant, **validated_data
        )

        return favorite_list


class PrivateFavoriteSerializer(serializers.ModelSerializer):
    job = JobListSerializer()

    class Meta:
        model = FavoriteList
        fields = [
            "uid",
            "applicant",
            "job",
            "created_at",
            "updated_at",
        ]
