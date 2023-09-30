from django.urls import path

from organization.rest.views import we


urlpatterns = [
    path("/users", we.OrganizationUserListCreateView.as_view()),
    path("/users/<uuid:uid>", we.OrganizationUserDetailView.as_view()),
]
