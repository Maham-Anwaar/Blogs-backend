# Django
from db_data.abstract_models.assignment_file import AssignmentFileAwareOnetoOneModel

# Backend Apps
from db_data.abstract_models.misc import ID, Dates, Name
from db_data.abstract_models.workshop import WorkshopAwareModel
from django.db import models


class Assignment(Dates, ID, Name, AssignmentFileAwareOnetoOneModel, WorkshopAwareModel):
    """This model stores the assignment details."""

    total_marks = models.IntegerField(default=10)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "assignment"
