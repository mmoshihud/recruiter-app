from rest_framework import generics
from core.rest.permission import IsNotOrganizationUser
from job.models import FavoriteList, Job
from me.rest.serializers.application import ApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from me.rest.serializers.job import (
    PrivateFavoriteCreateSerializer,
    PrivateFavoriteSerializer,
)


from organization.rest.serializers.job import JobSerializer

from rest_framework.permissions import IsAuthenticated


class PrivateApplyForJob(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


class PrivateJobList(generics.ListAPIView):
    queryset = Job.objects.filter()
    serializer_class = JobSerializer
    permission_classes = [IsNotOrganizationUser]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["job_type"]
    search_fields = ["title"]


class PrivateFavoriteCreate(generics.CreateAPIView):
    serializer_class = PrivateFavoriteCreateSerializer
    permission_classes = [IsNotOrganizationUser]


class PrivateFavoriteList(generics.ListAPIView):
    serializer_class = PrivateFavoriteSerializer
    permission_classes = [IsNotOrganizationUser]

    def get_queryset(self):
        user = self.request.user
        queryset = FavoriteList.objects.filter(applicant=user)

        return queryset


class PrivateFavoriteDetail(generics.DestroyAPIView):
    queryset = FavoriteList.objects.filter()
    serializer_class = PrivateFavoriteSerializer
    permission_classes = [IsNotOrganizationUser]
