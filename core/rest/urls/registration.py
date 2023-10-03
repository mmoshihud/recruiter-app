from django.urls import path, include

from me.rest.views import user


urlpatterns = [
    path("", user.PublicUserCreate.as_view()),
]
