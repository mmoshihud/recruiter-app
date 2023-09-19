from django.urls import path
from core.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("me/create/", UserCreateView.as_view()),
    path("token/", obtain_auth_token),
    path("we/user/create/", OrganizationUserView.as_view()),
    path("we/create/", OrganizationCreateView.as_view()),
    path("we/<int:pk>", OrganizationDetailView.as_view()),
]
