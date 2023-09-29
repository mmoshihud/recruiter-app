from common.choices import StatusChoices
from django.db import models
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=StatusChoices.choices, default="Active"
    )

    class Meta:
        abstract = True
