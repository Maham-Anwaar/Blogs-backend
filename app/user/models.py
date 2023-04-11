from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    @property
    def return_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.return_full_name
