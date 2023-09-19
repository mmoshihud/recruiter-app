from django.urls import path
from job import views

urlpatterns = [
    path("job/", views.JobListView.as_view()),
    path("job/create/", views.JobListCreateView.as_view()),
    path("job/<int:pk>/", views.JobDetailView.as_view()),
    path("application/", views.ApplicationListView.as_view()),
    path("application/create/", views.ApplicationCreateView.as_view()),
    path("application/<int:pk>/", views.ApplicationDetailView.as_view()),
]
