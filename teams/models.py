from django.db import models
from accounts.models import Profile as User
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teamleader =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='teams_led')
    members = models.ManyToManyField(User, related_name='teams')
    def __str__(self):
        return f'{self.name}'
