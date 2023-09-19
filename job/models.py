from django.db import models
from django.utils import timezone
from core.models import Organization


class Job(models.Model):
    title = models.CharField(max_length=255)
    vacancy = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posting_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    resume_url = models.URLField(max_length=200)
    application_date = models.DateTimeField(auto_now=True)
