from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin", admin.site.urls),
    path("api/auth", include("core.urls")),
    path("api/we", include("organization.urls")),
    path("api/job", include("job.urls")),
    path("auth", include("rest_framework.urls")),
]
