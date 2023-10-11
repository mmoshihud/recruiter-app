from django.db import models

from common.base import BaseModel
from core.models import User

from organization.models import Organization
from messaging.models import Thread


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    organization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, null=True, blank=True
    )
    job = models.ForeignKey("job.Job", on_delete=models.SET_NULL, null=True, blank=True)
    thread = models.ForeignKey(Thread, on_delete=models.SET_NULL, null=True, blank=True)
