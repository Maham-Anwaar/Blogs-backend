# Django
from django.db import models


class AssignmentFileAwareModel(models.Model):
    """
    This is an abstract class which contains a foreign key to the
    assignment file table.
    """

    assignment_file = models.ForeignKey(to="db_data.AssignmentFile", on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True


class AssignmentFileAwareOnetoOneModel(models.Model):

    assignment_file = models.OneToOneField(
        to="db_data.AssignmentFile", on_delete=models.CASCADE, related_name="%(class)s"
    )

    class Meta:
        abstract = True
