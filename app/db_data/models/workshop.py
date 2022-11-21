# Django
from db_data.abstract_models.base_user import BaseUserAwareModel

# Backend Apps
from db_data.abstract_models.misc import ID, Dates, Name, StartEndDate
from db_data.choices.level import LevelChoices
from db_data.choices.mode import ModeChoices
from django.db import models


class Workshop(Dates, ID, Name, StartEndDate, BaseUserAwareModel):
    """This model stores the workshop details."""

    level = models.CharField(choices=LevelChoices.choices, max_length=25)
    mode = models.CharField(choices=ModeChoices.choices, max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "workshop"
