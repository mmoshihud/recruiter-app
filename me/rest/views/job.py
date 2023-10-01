from rest_framework import generics
from core.rest.permission import IsNotOrganizationUser
from job.models import Job
from me.rest.serializers.application import ApplicationSerializer

from organization.rest.serializers.job import JobSerializer

from rest_framework.permissions import IsAuthenticated


class ApplyForJob(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsNotOrganizationUser]
