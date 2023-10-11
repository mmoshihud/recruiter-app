from django.urls import path
from messaging.rest.views import message

urlpatterns = [
    path("/threads/c/<uuid:thread_uid>", message.PrivateThreadDetail.as_view()),
    path("/threads/<uuid:organization_uid>", message.PrivateThreadCreate.as_view()),
]
