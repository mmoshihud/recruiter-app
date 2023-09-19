from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    vacancy = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posting_date = models.DateField()
    expiration_date = models.DateField()
