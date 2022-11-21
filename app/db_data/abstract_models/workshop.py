# Django
from django.db import models


class WorkshopAwareOnetoOneModel(models.Model):

    workshop = models.OneToOneField(to="db_data.Workshop", on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True


class WorkshopAwareModel(models.Model):

    workshop = models.ForeignKey(to="db_data.Workshop", on_delete=models.CASCADE, related_name="%(class)s")

    class Meta:
        abstract = True
