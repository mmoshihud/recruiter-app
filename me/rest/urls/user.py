from django.urls import path

from me.rest.views import user


urlpatterns = [
    path("/profile", user.PrivateUserProfileUpdate.as_view()),
]
