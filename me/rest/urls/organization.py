from django.urls import path

from me.rest.views import organization


urlpatterns = [
    path("/organizations", organization.OrganizationList.as_view()),
    path(
        "/organizations/<uuid:organization_uuid>/jobs",
        organization.OrganizationJobList.as_view(),
    ),
]
