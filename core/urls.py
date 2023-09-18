from django.urls import path
from core.views import CreateUserView, OrganizationUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("me/create/", CreateUserView.as_view()),
    path("token/", obtain_auth_token),
    path("we/create/", OrganizationUserView.as_view()),
]
