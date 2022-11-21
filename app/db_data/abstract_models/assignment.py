# Django
from django.db import models


class AssignmentAwareOnetoOneModel(models.Model):
    """
    This is an abstract class which contains a O2O relation to the 
    assignment table.
    """

    applicant = models.OneToOneField(
        to="db_data.Assignment", on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    class Meta:
        abstract = True


class AssignmentAwareModel(models.Model):
    """
    This is an abstract class which contains a foreign key to the 
    BaseUser table.
    """

    assignment = models.ForeignKey(
        to="db_data.Assignment", on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    class Meta:
        abstract = True
