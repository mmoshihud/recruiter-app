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
