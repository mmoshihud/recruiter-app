from django.urls import path

from organization.rest.views import we


urlpatterns = [
    path("/users", we.PrivateOrganizationUserList.as_view()),
    path("/users/<uuid:uid>", we.PrivateOrganizationUserDetail.as_view()),
]
