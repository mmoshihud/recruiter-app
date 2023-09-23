from django.urls import path

from applicant import views


urlpatterns = [
    path("/organizations", views.OrganizationList.as_view()),
    path("/organizations/<int:pk>/jobs", views.OrganizationJobList.as_view()),
    path("/jobs/<int:job_id>/apply", views.ApplyForJob.as_view()),
]
