# Django
from db_data.abstract_models.material import MaterialAwareOnetoOneModel

# Backend Apps
from db_data.abstract_models.misc import ID, Dates, Name
from db_data.abstract_models.workshop import WorkshopAwareModel
from django.db import models


class Lecture(Dates, ID, Name, MaterialAwareOnetoOneModel, WorkshopAwareModel):
    """This model stores the lecture details."""

    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "lecture"
