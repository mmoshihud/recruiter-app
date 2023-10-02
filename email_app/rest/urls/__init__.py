from django.urls import path
from email_app.rest.views.email import EmailView

urlpatterns = [
    path("", EmailView.as_view(), name="send-email"),
]
