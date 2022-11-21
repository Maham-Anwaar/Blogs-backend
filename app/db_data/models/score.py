# Django
from django.db import models

# Backend Apps
from db_data.abstract_models.misc import ID, Dates, Name
from db_data.abstract_models.student import StudentAwareModel
from db_data.abstract_models.assignment import AssignmentAwareModel


class Score(Dates, ID, Name, StudentAwareModel, AssignmentAwareModel):
    """This model stores the score per assignment of each student."""

    score = models.IntegerField(default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "score"
