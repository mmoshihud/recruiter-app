from django.urls import path

from core import views
from core.auth import CustomAuthToken


urlpatterns = [
    path("/token", CustomAuthToken.as_view()),
    path("/registration", views.UserCreateView.as_view()),
    path("/organizations", views.OrganizationListCreateView.as_view()),
    path(
        "/organizations/<uuid:organization_uuid>",
        views.OrganizationDetailView.as_view(),
    ),
    path("/organizations/onboard", views.OrganizationOnboardView.as_view()),
]
