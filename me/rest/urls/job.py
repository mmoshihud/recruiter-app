from django.urls import path

from me.rest.views import job


urlpatterns = [
    path("", job.PrivateJobList.as_view()),
    path("/<uuid:job_uid>/apply", job.PrivateApplyForJob.as_view()),
    path("/<uuid:job_uid>/favorite", job.PrivateFavoriteCreate.as_view()),
    path("/favorites/<uuid:favorite_uid>", job.PrivateFavoriteDetail.as_view()),
    path("/favorites", job.PrivateFavoriteList.as_view()),
]
