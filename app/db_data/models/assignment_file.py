# Django
from django.db import models

# Backend Apps
from db_data.abstract_models.misc import ID, Dates
from db_data.uploadpaths import upload_assignment_file
from db_data.validations import file_validation


class AssignmentFile(Dates, ID):
    """This model stores the assignment files uploaded by the user."""

    file = models.FileField(upload_to=upload_assignment_file,
                            validators=[file_validation])
    # it's actually the mime type of the file. Or the content type.
    # Like image/png etc.
    file_type = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = "assignmentfile"
