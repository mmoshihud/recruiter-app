from django.urls import path
from job.views import (
    ApplicationCreateView,
    ApplicationListView,
    JobListCreateView,
    JobDetailView,
    JobListView,
)


urlpatterns = [
    path("job/", JobListView.as_view()),
    path("job/create/", JobListCreateView.as_view()),
    path("job/<int:pk>", JobDetailView.as_view()),
    path("application/", ApplicationListView.as_view()),
    path("application/create", ApplicationCreateView.as_view()),
]
