from rest_framework import generics
from common.choices import StatusChoices
from core.rest.permission import IsNotOrganizationUser
from organization.models import Organization
from job.models import Job
from organization.rest.serializers.organization import OrganizationSerializer
from organization.rest.serializers.job import JobSerializer


class PrivateOrganizationList(generics.ListAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSerializer
    permission_classes = [IsNotOrganizationUser]


class PrivateOrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSerializer
    permission_classes = [IsNotOrganizationUser]

    def perform_destroy(self, instance):
        instance.status = StatusChoices.REMOVED
        instance.save()


class PrivateOrganizationJobList(generics.ListAPIView):
    queryset = Job.objects.filter()
    serializer_class = JobSerializer
    permission_classes = [IsNotOrganizationUser]

    def get_queryset(self):
        organization_uid = self.kwargs.get("organization_uid")
        organization = Organization.objects.get(uid=organization_uid)
        return Job.objects.filter(organization_id=organization)
