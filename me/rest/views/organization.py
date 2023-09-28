from rest_framework import generics
from organization.models import Organization
from job.models import Job
from organization.rest.serializers import OrganizationSerializer
from organization.rest.serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class OrganizationJobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        organization_uuid = self.kwargs.get("organization_uuid")
        organization = Organization.objects.get(uuid=organization_uuid)
        return Job.objects.filter(organization_id=organization)
