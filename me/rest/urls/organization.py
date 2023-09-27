from django.urls import path

from applicant import views


urlpatterns = [
    path("/organizations", views.OrganizationList.as_view()),
    path(
        "/organizations/<uuid:organization_uuid>/jobs",
        views.OrganizationJobList.as_view(),
    ),
]
