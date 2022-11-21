# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class ModeChoices(models.TextChoices):
    """Allowed modes of a workshop."""

    ONLINE = "online", _("online")
    ONSITE = "onsite", _("onsite")
