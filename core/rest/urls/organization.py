from django.urls import path

from core.rest.views import organization


urlpatterns = [
    path("", organization.PrivateOrganizationList.as_view()),
    path("/<uuid:organization_uid>", organization.PrivateOrganizationDetail.as_view()),
    path("/onboard", organization.PrivateOrganizationOnboard.as_view()),
]
