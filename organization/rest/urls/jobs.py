from django.urls import path

from organization.rest.views import job

urlpatterns = [
    path("", job.PrivateJobList.as_view()),
    path("/<uuid:uid>", job.PrivateJobDetail.as_view()),
    path("/applications", job.PrivateAppliedJobsList.as_view()),
    path(
        "/applications/<uuid:application_uid>/feedback",
        job.PrivateFeedbackList.as_view(),
    ),
    path(
        "/applications/<uuid:application_uid>/feedback/<uuid:feedback_uid>",
        job.PrivateFeedbackDetail.as_view(),
    ),
]
