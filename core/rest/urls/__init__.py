from django.urls import path, include


urlpatterns = [
    path("/registration", include("core.rest.urls.registration")),
    path("/token", include("core.rest.urls.auth")),
]
