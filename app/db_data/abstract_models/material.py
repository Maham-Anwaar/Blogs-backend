# Django
from django.db import models


class MaterialAwareModel(models.Model):
    """
    This is an abstract class which contains a foreign key to the
    material table.
    """

    material = models.ForeignKey(to="db_data.Material", on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True


class MaterialAwareOnetoOneModel(models.Model):
    material = models.OneToOneField(to="db_data.Material", on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True
