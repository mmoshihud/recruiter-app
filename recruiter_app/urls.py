from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("admin", admin.site.urls),
    path("api/auth", include("core.urls")),
    path("api/we", include("organization.urls")),
    path("api/we/jobs", include("job.urls")),
    path("api/me", include("applicant.urls")),
    path("auth", include("rest_framework.urls")),
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
]
