from django.db import models
from datetime import datetime
from accounts.models import Profile as User
# Create your models here.
class Application(models.Model):
    bid = models.CharField(max_length=100, default=0)
    cover_letter = models.TextField(default=None)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate')
    date_created = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    responsibilities = models.TextField(default=None)
    skills = models.TextField(default=None)
    payment = models.CharField(max_length=100, default=0)
    bids = models.IntegerField(default=0)
    is_it_done = models.BooleanField(default=False)
    creator =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_created')
    date_created = models.DateTimeField(auto_now_add=True)
    applications = models.ManyToManyField(Application, related_name='apllications')
    is_it_paid = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'
