from django.db import models
from common.base import BaseModel

from core.models import User
from organization.choices import RoleChoices


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OrganizationUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)

    def __str__(self):
        return f"{self.user.email} - {self.role} at {self.organization}"
