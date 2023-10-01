from django.urls import path, include

from core.rest.views import user


urlpatterns = [
    path("/users", user.PrivateUserList.as_view()),
    path("/registration", user.PublicUserCreate.as_view()),
    path("/token", include("core.rest.urls.auth")),
    path("/organizations", include("core.rest.urls.organization")),
]
