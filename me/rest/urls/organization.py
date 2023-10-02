from django.urls import path

from me.rest.views import organization


urlpatterns = [
    path("/organizations", organization.PrivateOrganizationList.as_view()),
    path(
        "/organizations/<uuid:organization_uid>/jobs",
        organization.PrivateOrganizationJobList.as_view(),
    ),
]
