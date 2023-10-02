from django.urls import path

from core.rest.views import user


urlpatterns = [
    path("", user.PrivateUserList.as_view()),
    path("/profile", user.PrivateUserProfileUpdate.as_view()),
]
