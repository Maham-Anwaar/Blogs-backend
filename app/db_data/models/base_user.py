# Django
# 3rd Party Libraries
import pytz

# Backend Apps
from db_data.abstract_models.misc import ID, Dates
from db_data.choices.role import RoleChoices
from db_data.managers.base_user import CustomBaseUserManager
from db_data.validations import email_validation, phone_validation, timezone_validation
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class BaseUser(AbstractBaseUser, PermissionsMixin, Dates, ID):
    email = models.CharField(max_length=255, unique=True, validators=[email_validation])
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=17, blank=True, validators=[phone_validation])
    timezone_name = models.CharField(default=pytz.utc.zone, max_length=50, validators=[timezone_validation])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    role = models.CharField(choices=RoleChoices.choices, max_length=25)

    objects = CustomBaseUserManager()
    USERNAME_FIELD = "email"

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.full_name
