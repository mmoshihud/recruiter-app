from django.urls import path
from email_app.rest.views import EmailView

urlpatterns = [
    path("/send-email", EmailView.as_view(), name="send-email"),
]
