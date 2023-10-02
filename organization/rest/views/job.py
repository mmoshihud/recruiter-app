from django.shortcuts import get_object_or_404
from rest_framework import generics

from core.rest.permission import IsOrganizationMember, IsOwnerAdminPermission
from job.models import Application, Feedback, Job
from organization.rest.serializers.job import (
    ApplicationSerializer,
    FeedbackDetailSerializer,
    FeedbackSerializer,
    JobSerializer,
)
from organization.models import Organization, OrganizationUser
from rest_framework.exceptions import ValidationError


class PrivateJobList(generics.ListCreateAPIView):
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


class PrivateJobDetail(generics.RetrieveUpdateDestroyAPIView):
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


class PrivateAppliedJobsList(generics.ListAPIView):
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


class PrivateFeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsOrganizationMember]


class PrivateFeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackDetailSerializer
    permission_classes = [IsOrganizationMember]

    def get_object(self):
        application_uid = self.kwargs.get("application_uid")
        feedback_uid = self.kwargs.get("feedback_uid")

        try:
            application = Application.objects.get(uid=application_uid)
        except Application.DoesNotExist:
            raise ValidationError("Application does not exist.")

        try:
            feedback = Feedback.objects.get(uid=feedback_uid, application=application)
            return feedback
        except Feedback.DoesNotExist:
            raise ValidationError("Feedback does not exist for this application.")
