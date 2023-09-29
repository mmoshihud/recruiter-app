from django.urls import path

from organization.rest.views import job

urlpatterns = [
    path("", job.JobListCreateView.as_view()),
    path("/<uuid:uuid>", job.JobDetailView.as_view()),
    path("/applications", job.AppliedJobsView.as_view()),
    path(
        "/applications/<uuid:application_uid>/feedback",
        job.FeedbackListCreateView.as_view(),
    ),
]
