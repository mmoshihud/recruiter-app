from django.urls import path
from email_app.rest.views import EmailView

urlpatterns = [
    path("", EmailView.as_view(), name="send-email"),
]
