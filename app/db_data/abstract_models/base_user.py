# Django
from django.db import models


class BaseUserAwareOnetoOneModel(models.Model):
    """
    This is an abstract class which contains a O2O relation to
    the BaseUser table.
    """

    user = models.OneToOneField(
        to="db_data.BaseUser", on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    class Meta:
        abstract = True


class BaseUserAwareModel(models.Model):
    """
    This is an abstract class which contains a foreign key to the 
    BaseUser table.
    """

    user = models.ForeignKey(
        to="db_data.BaseUser", on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    class Meta:
        abstract = True
