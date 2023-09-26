from django.urls import path

from job import views

urlpatterns = [
    path("", views.JobListCreateView.as_view()),
    path("/<uuid:uuid>", views.JobDetailView.as_view()),
    path("/application", views.AppliedJobsView.as_view()),
    path(
        "/application/feedback/<uuid:application_uuid>",
        views.FeedbackListCreateView.as_view(),
    ),
]
