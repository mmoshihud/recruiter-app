from django.urls import path

from me.rest.views import job


urlpatterns = [
    path("/jobs", job.JobList.as_view()),
    path("/jobs/<uuid:job_uid>/apply", job.ApplyForJob.as_view()),
]
