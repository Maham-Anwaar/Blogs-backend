# Django
from django.db import models


class LectureAwareOnetoOneModel(models.Model):
    """
    This is an abstract class which contains a O2O relation to the
    lecture table.
    """

    lecture = models.OneToOneField(to="db_data.Lecture", on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True


class LectureAwareModel(models.Model):
    """
    This is an abstract class which contains a foreign key to the
    lecture table.
    """

    lecture = models.ForeignKey(to="db_data.Lecture", on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True
