# Django
from django.db import models


class StudentAwareOnetoOneModel(models.Model):
    """
    This is an abstract class which contains a O2O relation to the
    student table.
    """

    student = models.OneToOneField(
        to="db_data.Student", on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    class Meta:
        abstract = True


class StudentAwareModel(models.Model):
    """
    This is an abstract class which contains a foreign key to the
    student table.
    """

    student = models.ForeignKey(
        to="db_data.Student", on_delete=models.CASCADE,
        related_name="%(class)s"
    )

    class Meta:
        abstract = True
