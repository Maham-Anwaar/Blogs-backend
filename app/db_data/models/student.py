# Backend Apps
from db_data.abstract_models.misc import ID, Dates, Name
from db_data.abstract_models.workshop import WorkshopAwareModel


class Student(Dates, ID, Name, WorkshopAwareModel):
    """This model stores the student details."""

    def __str__(self):
        return self.name

    class Meta:
        db_table = "student"
