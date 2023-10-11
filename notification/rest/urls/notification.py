from django.urls import path

from notification.rest.views.notification import PrivateNotificationList


urlpatterns = [
    path("", PrivateNotificationList.as_view()),
]
