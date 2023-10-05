from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("admin", admin.site.urls),
    path("api/auth", include("core.rest.urls")),
    path("api/organizations", include("core.rest.urls.organization")),
    path("api/we", include("organization.rest.urls")),
    path("api/me", include("me.rest.urls")),
    path("api/messages", include("messaging.rest.urls")),
]
