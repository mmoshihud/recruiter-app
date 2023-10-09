from django.urls import path
from messaging.rest.views import message

urlpatterns = [
    path("/threads", message.PrivateThreadList.as_view()),
    path("/threads/<uuid:thread_uid>", message.PrivateThreadDetail.as_view()),
    path("/threads/c/<uuid:organization_uid>", message.PrivateThreadCreate.as_view()),
]
