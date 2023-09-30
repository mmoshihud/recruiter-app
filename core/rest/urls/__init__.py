from django.urls import path

from core.rest import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("/registration", views.UserCreateView.as_view()),
    path("/organizations", views.OrganizationListCreateView.as_view()),
    path(
        "/organizations/<uuid:organization_uid>",
        views.OrganizationDetailView.as_view(),
    ),
    path("/organizations/onboard", views.OrganizationOnboardView.as_view()),
    path("/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("/token/verify", TokenVerifyView.as_view(), name="token_verify"),
]
