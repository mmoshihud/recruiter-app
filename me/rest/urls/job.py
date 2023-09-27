from django.urls import path

from applicant import views


urlpatterns = [
    path("/jobs/<uuid:job_uuid>/apply", views.ApplyForJob.as_view()),
]
