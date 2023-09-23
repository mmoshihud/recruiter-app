from rest_framework import generics
from organization.models import Organization
from job.models import Job
from organization.serializer import OrganizationSerializer
from job.serializer import ApplicationSerializer, JobSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationJobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        organization_pk = self.kwargs.get("pk")
        return Job.objects.filter(organization_id=organization_pk)


class ApplyForJob(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
