# DRF
# Backend Apps
from db_data.choices.role import RoleChoices
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """This permission class checks whether the user is Admin or not."""

    def has_permission(self, request, view):
        if request.user.role in [RoleChoices.ADMIN, RoleChoices.OWNER]:
            return True

        return False


class IsOwner(permissions.BasePermission):
    """This permission class checks whether the user is Owner or not."""

    def has_permission(self, request, view):
        if request.user.role == RoleChoices.OWNER:
            return True

        return False
