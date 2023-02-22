from django.db import models
from datetime import datetime
from accounts.models import Profile as User
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    responsibilities = models.TextField(default=None)
    skills = models.TextField(default=None)
    payment = models.IntegerField()
    bids = models.IntegerField(default=0)
    is_it_done = models.BooleanField(default=False)
    creator =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    date_created = models.DateTimeField(auto_now_add=True)
    is_it_paid = models.BooleanField(default=False)
    currency = models.CharField(max_length=5)
    payment_type_hourly = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'

class Application(models.Model):
    bid = models.IntegerField()
    cover_letter = models.TextField(default=None)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate')
    date_created = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project', null=True)
    currency = models.CharField(max_length=5)