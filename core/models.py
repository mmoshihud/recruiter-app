from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _
from common.base import BaseModel

from core.managers import UserManager
from organization.models import OrganizationUser


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def get_organization(self):
        try:
            organization_user = self.organizationuser_set.filter(
                is_default=True
            ).first()

            if organization_user:
                return organization_user.organization
            return None
        except OrganizationUser.DoesNotExist:
            return None

    def __str__(self):
        return self.email
