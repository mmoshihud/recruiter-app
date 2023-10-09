from django.urls import path
from messaging.rest.views import message

urlpatterns = [
    path("", message.PrivateMessageCreate.as_view()),
    path("/inbox", message.PrivateInboxList.as_view()),
    path("/<uuid:inbox_uid>", message.PrivateMessageDetail.as_view()),
    path("/thread/<uuid:organization_uid>", message.PrivateThreadCreate.as_view()),
]
