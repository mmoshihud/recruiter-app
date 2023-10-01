from django.urls import path

from core.rest.views import organization


urlpatterns = [
    path("", organization.OrganizationListCreateView.as_view()),
    path("/<uuid:organization_uid>", organization.OrganizationDetailView.as_view()),
    path("/onboard", organization.OrganizationOnboardView.as_view()),
]
