from django.urls import path

from job import views

urlpatterns = [
    path("", views.JobListCreateView.as_view()),
    path("/<int:pk>", views.JobDetailView.as_view()),
    path("/application", views.AppliedJobsView.as_view()),
    path("/application/feedback/<int:app_id>", views.FeedbackListCreateView.as_view()),
]
