from django.urls import path
from job.views import JobListCreateView


urlpatterns = [
    path("job/create/", JobListCreateView.as_view()),
]
