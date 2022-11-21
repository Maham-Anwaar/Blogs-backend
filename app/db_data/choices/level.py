# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class LevelChoices(models.TextChoices):
    """Allowed modes of a workshop."""

    ONE = "one", _("one")
    TWO = "two", _("two")
    THREE = "three", _("three")
    FOUR = "four", _("four")
