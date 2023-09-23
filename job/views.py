from rest_framework import generics

from core.permission import IsOwnerAdminPermission
from job.models import Application, Feedback, Job, Offer
from job.serializer import (
    ApplicationSerializer,
    FeedbackSerializer,
    JobSerializer,
    OfferSerializer,
)


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerAdminPermission]


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerAdminPermission]


class AppliedJobsView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicantFeedback(generics.CreateAPIView):
    serializer_class = ApplicationSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


""" 
class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
"""
