from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    
    def create_account(self, email, password=None, **extra_fields):
        """Creates & saves a new user."""
        if not email:
            raise ValueError("Users must have an email address!")
        account = self.model(email=self.normalize_email(email), **extra_fields)
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(self, email, password, **kwargs):
        """Create and saves a new super user."""
        account = self.create_account(email, password, **kwargs)
        account.is_active = True
        account.is_staff = True
        account.is_superuser = True
        account.save(using=self._db)
        return account

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    @property
    def return_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.return_full_name
