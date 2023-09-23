from rest_framework import generics

from core.permission import IsOrganizationMember, IsOwnerAdminPermission
from job.models import Application, Feedback, Job
from job.serializer import (
    ApplicationSerializer,
    FeedbackSerializer,
    JobSerializer,
)
from organization.models import OrganizationUser


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerAdminPermission]


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerAdminPermission]


class AppliedJobsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsOrganizationMember]

    def get_queryset(self):
        user = self.request.user
        organization_user = OrganizationUser.objects.filter(user=user).first()

        if organization_user:
            organization = organization_user.organization

            users_in_organization = OrganizationUser.objects.filter(
                organization=organization
            )
            user_objects = [
                organization_user.user for organization_user in users_in_organization
            ]
            queryset = Application.objects.filter(applicant__in=user_objects)
        else:
            queryset = Application.objects.none()

        return queryset


class ApplicantFeedback(generics.CreateAPIView):
    serializer_class = ApplicationSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
