from django.db import models

from common.base import BaseModel
from core.models import User
from job.models import Job
from organization.models import Organization


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)


class NotificationConnector(BaseModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, null=True, blank=True
    )
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
