from django.urls import path, include

from core.rest.views import user


urlpatterns = [
    path("/registration", user.PublicUserCreate.as_view()),
    path("/users", include("core.rest.urls.user")),
    path("/token", include("core.rest.urls.auth")),
    path("/organizations", include("core.rest.urls.organization")),
]
