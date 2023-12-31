from django.shortcuts import get_object_or_404
from rest_framework import generics
from common.choices import StatusChoices

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


class PrivateOrganizationJobList(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        organization_uid = self.kwargs["organization_uid"]

        OrganizationUser.objects.filter(user=self.request.user).update(is_default=False)

        organization_user = get_object_or_404(
            OrganizationUser, user=self.request.user, organization__uid=organization_uid
        )
        organization_user.is_default = True
        organization_user.save()

        organization = self.request.user.get_organization()

        if organization:
            return Job.objects.filter(organization=organization)
        return None


class PrivateJobList(generics.ListCreateAPIView):
    queryset = Job.objects.filter()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOwnerAdminPermission()]
        return [IsOrganizationMember()]

    def get_queryset(self):
        user = self.request.user
        organization = user.get_organization()

        if organization:
            return Job.objects.filter(organization=organization)
        return None


class PrivateJobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.filter()
    serializer_class = JobSerializer
    lookup_field = "uid"
    permission_classes = [IsOwnerAdminPermission]

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsOrganizationMember()]
        elif self.request.method in ("PUT", "PATCH", "DELETE"):
            return [IsOwnerAdminPermission()]
        return super().get_permissions()

    def perform_destroy(self, instance):
        instance.status = StatusChoices.REMOVED
        instance.save()


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
            queryset = None
        return queryset


class PrivateFeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.filter()
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
