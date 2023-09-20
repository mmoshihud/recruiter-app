from django.urls import path

from job import views

urlpatterns = [
    path("", views.JobListCreateView.as_view()),
    path("<int:pk>/", views.JobDetailView.as_view()),
    path("application/", views.ApplicationListCreateView.as_view()),
    path("application/<int:ok>/", views.ApplicationDetailView.as_view()),
    path("offer/", views.OfferListCreateView.as_view()),
    path("offer/<int:pk>/", views.OfferDetailView.as_view()),
]
