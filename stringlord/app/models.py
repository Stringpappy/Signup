from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
"""
class CustomUser(AbstractUser):
    '''Custom user model that supports email as the username'''
    email = models.EmailField(unique=True)  # Use email for authentication                    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def __str__(self):
        return self.email

class Client(models.Model):
    '''Model for clients.'''
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    service_needed = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Client)"

class ServiceProvider(models.Model):
    '''Model for service providers.'''
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    working_hour = models.CharField(max_length=100)  # e.g., "9am-5pm"
    professions = models.CharField(max_length=255)  # e.g., "Plumber, Electrician"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Service Provider)"


"""




from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user model that supports email as the username."""
    email = models.EmailField(unique=True)  # Use email for authentication
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    # Add related_name to prevent conflicts with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Customize the reverse accessor
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Customize the reverse accessor
        blank=True
    )

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class Client(models.Model):
    """Model for clients."""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    service_needed = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Client)"

class ServiceProvider(models.Model):
    """Model for service providers."""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    working_hour = models.CharField(max_length=100)  # e.g., "9am-5pm"
    professions = models.CharField(max_length=255)  # e.g., "Plumber, Electrician"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Service Provider)"

