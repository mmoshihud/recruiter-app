from django.db import models
from django.utils import timezone
from common.base import BaseModel

from core.models import User
from job.choices import JobTypeChoices
from organization.models import Organization


class Job(BaseModel):
    title = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255, choices=JobTypeChoices.choices)
    vacancy = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    job_poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    resume_url = models.URLField(max_length=200)
    application_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feedback(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    feedback_description = models.TextField()
    feedback_rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.application.applicant.name} - Applied at {self.application.job.organization} in {self.application.job.title} Position"


class FavoriteList(BaseModel):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
