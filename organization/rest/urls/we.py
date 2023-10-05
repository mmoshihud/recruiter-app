from django.urls import path

from organization.rest.views import we
from organization.rest.views import job


urlpatterns = [
    path("/users", we.PrivateOrganizationUserList.as_view()),
    path("/users/<uuid:uid>", we.PrivateOrganizationUserDetail.as_view()),
    path("/<uuid:organization_uid>/jobs", job.PrivateOrganizationJobList.as_view()),
]
