from django.urls import path
from core import views
from core.auth import CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("me/create/", views.UserCreateView.as_view()),
    path("token/", CustomAuthToken.as_view()),
    path("we/user/create/", views.OrganizationUserView.as_view()),
    path("we/create/", views.OrganizationCreateView.as_view()),
    path("we/<int:pk>/", views.OrganizationDetailView.as_view()),
]
