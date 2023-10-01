from rest_framework import generics
from core.rest.permission import IsNotOrganizationUser
from organization.models import Organization
from job.models import Job
from organization.rest.serializers.organization import OrganizationSerializer
from organization.rest.serializers.job import JobSerializer


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsNotOrganizationUser]


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsNotOrganizationUser]


class OrganizationJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsNotOrganizationUser]

    def get_queryset(self):
        organization_uid = self.kwargs.get("organization_uid")
        organization = Organization.objects.get(uid=organization_uid)
        return Job.objects.filter(organization_id=organization)
