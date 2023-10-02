from django.urls import path

from me.rest.views import job


urlpatterns = [
    path("/jobs", job.PrivateJobList.as_view()),
    path("/jobs/<uuid:job_uid>/apply", job.PrivateApplyForJob.as_view()),
]
