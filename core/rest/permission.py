from rest_framework import permissions
from organization.models import OrganizationUser
from django.contrib.auth.models import AnonymousUser


class IsOwnerAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_authenticated:
            return user.organizationuser_set.filter(
                role__in=["OWNER", "ADMIN"]
            ).exists()
        return False


class IsOrganizationMember(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_authenticated:
            return user.organizationuser_set.filter(
                role__in=["OWNER", "ADMIN", "MANAGER", "HR"]
            ).exists()
        return False


class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_authenticated:
            return user.is_superuser
        return False


class IsNotOrganizationUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if isinstance(user, AnonymousUser):
            return False

        if user.is_superuser:
            return False

        return not OrganizationUser.objects.filter(user=user).exists()
