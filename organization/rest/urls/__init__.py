from django.urls import path, include

urlpatterns = [
    path("/jobs", include("organization.rest.urls.jobs")),
    path("", include("organization.rest.urls.we")),
]