from django.urls import path, include

urlpatterns = [
    path("/jobs", include("me.rest.urls.job")),
    path("", include("me.rest.urls.organization")),
    path("", include("me.rest.urls.user")),
]
