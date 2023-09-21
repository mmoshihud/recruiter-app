from django.urls import path

from organization import views


urlpatterns = [
    path("/users", views.OrganizationUserCreateView.as_view()),
    path("/users/<int:pk>", views.OrganizationUserDetailView.as_view()),
]
