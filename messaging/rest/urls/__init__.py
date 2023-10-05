from django.urls import path, include

urlpatterns = [
    path("", include("messaging.rest.urls.message")),
]
