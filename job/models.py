from django.db import models
from django.utils import timezone

from core.models import User
from organization.models import Organization
import uuid


class Job(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    vacancy = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posting_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    job_poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    resume_url = models.URLField(max_length=200)
    application_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    feedback_description = models.TextField()
    feedback_rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.application.applicant.name} - Applied at {self.application.job.organization} in {self.application.job.title} Position"
