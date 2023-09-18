from django.urls import path
from core.views import CreateUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("create/", CreateUserView.as_view()),
    path("token/", obtain_auth_token),
]
