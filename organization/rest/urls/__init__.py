from django.urls import path, include

urlpatterns = [
    path("", include("organization.rest.urls.we")),
    path("/jobs", include("organization.rest.urls.jobs")),
    path("/email", include("email_app.rest.urls")),
]
