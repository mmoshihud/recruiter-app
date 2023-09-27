from django.urls import path, include

urlpatterns = [
    path("", include("me.rest.urls.job")),
    path("", include("me.rest.urls.organization")),
]
