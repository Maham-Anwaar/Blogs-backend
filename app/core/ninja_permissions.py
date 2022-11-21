# Standard Library
# from typing import Optional

# Backend Apps
from core.constants import A_401_AUTH_FAILED, P_403_ADMIN, P_403_LOGGED_IN, P_403_OWNER
from db_data.choices.role import RoleChoices
from db_data.models.base_user import BaseUser

# 3rd Party Libraries
from ninja.errors import HttpError

# from pydantic import UUID4


def is_authenticated(user: BaseUser) -> bool:
    if user.is_anonymous:
        raise HttpError(401, A_401_AUTH_FAILED)
    return True


def is_logged_in(user: BaseUser) -> bool:
    if user.role:
        return True
    raise HttpError(403, P_403_LOGGED_IN)


def is_admin(user: BaseUser) -> bool:
    if user.role.role.type in [RoleChoices.ADMIN, RoleChoices.OWNER]:
        return True
    raise HttpError(403, P_403_ADMIN)


def is_owner(user: BaseUser) -> bool:
    if user.role.role.type == RoleChoices.OWNER:
        return True
    raise HttpError(403, P_403_OWNER)


def check_permission(perm: str, *args, **kwargs) -> bool:
    """This function helps check the specified permission for a user in a\
        specific tenant. It raises a permission denied\
        error if user isn't permitted."""
    perms = {
        "is_admin": is_admin,
        "is_owner": is_owner,
        "is_authenticated": is_authenticated,
    }

    return perms[perm](*args, **kwargs)
