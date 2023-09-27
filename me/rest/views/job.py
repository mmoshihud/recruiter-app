from rest_framework import generics

from job.serializer import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated


class ApplyForJob(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
