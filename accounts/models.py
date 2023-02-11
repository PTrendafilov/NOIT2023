from django.db import models
from django.contrib.auth.models import AbstractUser

# Create a custom user model to store additional information
class Profile(AbstractUser):
    # Define choices for the role field
    ROLE_CHOICES = (
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
        ('teamleader', 'Team Leader'),
    )
    
    # Add an email field with unique constraint
    email = models.EmailField(unique=True)
    
    # Add a points field with default value 0
    points = models.IntegerField(default=0)
    
    # Add a role field with choices defined above
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='freelancer')