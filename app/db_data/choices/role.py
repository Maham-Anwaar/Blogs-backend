# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoices(models.TextChoices):
    """Allowed roles in a tenant."""

    ADMIN = "admin", _("admin")
    MEMBER = "member", _("member")
    OWNER = "owner", _("owner")
