from core.models import User
from django.db import models

from common.base import BaseModel
from messaging.choices import KindChoices


class Thread(BaseModel):
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    kind = models.CharField(
        max_length=10, choices=KindChoices.choices, default=KindChoices.PARENT
    )
    author = models.ForeignKey("core.User", on_delete=models.CASCADE)
    content = models.TextField()
    organization = models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE
    )
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]


class Inbox(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    other_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="other_user_inbox"
    )

    def __str__(self):
        return f"From {self.user} to {self.other_user}"


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
