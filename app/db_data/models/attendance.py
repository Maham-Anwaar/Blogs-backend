# Django
from django.db import models

# Backend Apps
from db_data.abstract_models.misc import ID, Dates, Name
from db_data.abstract_models.student import StudentAwareModel
from db_data.abstract_models.lecture import LectureAwareModel


class Attendance(Dates, ID, Name, StudentAwareModel, LectureAwareModel):
    """This model stores the attendance per lecture of each student."""

    present = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "attendance"
