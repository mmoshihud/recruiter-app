from django.urls import path

from core import views
from core.auth import CustomAuthToken


urlpatterns = [
    path("/token", CustomAuthToken.as_view()),
    path("/registration", views.UserCreateView.as_view()),
    path("/organizations", views.OrganizationListCreateView.as_view()),
    path("/organizations/<int:pk>", views.OrganizationDetailView.as_view()),
]
