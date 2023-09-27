from django.urls import path

from me.rest.views import job


urlpatterns = [
    path("/jobs/<uuid:job_uuid>/apply", job.ApplyForJob.as_view()),
]
