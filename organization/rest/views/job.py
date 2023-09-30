from django.shortcuts import get_object_or_404
from rest_framework import generics

from core.rest.permission import IsOrganizationMember, IsOwnerAdminPermission
from job.models import Application, Feedback, Job
from organization.rest.serializers import (
    ApplicationSerializer,
    FeedbackSerializer,
    JobSerializer,
)
from organization.models import Organization, OrganizationUser


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOwnerAdminPermission()]
        return [IsOrganizationMember()]

    def get_queryset(self):
        user = self.request.user
        organization = Organization.objects.filter(organizationuser__user=user).first()

        if organization:
            return Job.objects.filter(organization=organization)
        return Job.objects.none()


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = "uid"
    permission_classes = [IsOwnerAdminPermission]

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsOrganizationMember()]
        elif self.request.method in ("PUT", "PATCH", "DELETE"):
            return [IsOwnerAdminPermission()]
        return super().get_permissions()


class AppliedJobsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsOrganizationMember]

    def get_queryset(self):
        user = self.request.user
        organization_user = OrganizationUser.objects.filter(user=user).first()

        if organization_user:
            organization = organization_user.organization
            jobs = Job.objects.filter(organization=organization)
            queryset = Application.objects.filter(job__in=jobs)
        else:
            queryset = Application.objects.none()
        return queryset


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsOrganizationMember]
