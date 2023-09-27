from django.urls import path

from job import views

urlpatterns = [
    path("", views.JobListCreateView.as_view()),
    path("/<uuid:uuid>", views.JobDetailView.as_view()),
    path("/applications", views.AppliedJobsView.as_view()),
    path(
        "/applications/<uuid:application_uuid>/feedback",
        views.FeedbackListCreateView.as_view(),
    ),
]
