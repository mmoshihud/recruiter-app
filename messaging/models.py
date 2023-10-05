from core.models import User
from django.db import models

from common.base import BaseModel


class Inbox(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    other_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="other_user_inbox"
    )


class Message(BaseModel):
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    content = models.TextField()

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content}"
