from django.urls import path

from core import views
from core.auth import CustomAuthToken


urlpatterns = [
    path("register/", views.UserCreateView.as_view()),
    path("token/", CustomAuthToken.as_view()),
    path("we/register/", views.OrganizationUserCreateView.as_view()),
    path("we/", views.OrganizationListCreateView.as_view()),
    path("we/<int:pk>/", views.OrganizationDetailView.as_view()),
]
