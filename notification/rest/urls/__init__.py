from django.urls import path, include

urlpatterns = [
    path("", include("notification.rest.urls.notification")),
]
