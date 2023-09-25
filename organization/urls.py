from django.urls import path

from organization import views


urlpatterns = [
    path("/users", views.OrganizationUserCreateView.as_view()),
    path("/users/<uuid:uuid>", views.OrganizationUserDetailView.as_view()),
]
