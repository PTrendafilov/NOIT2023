from django.db import models
from accounts.models import Profile as User

class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    company = models.CharField(max_length=100)

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    place = models.CharField(max_length=100)

class CV(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    about_me = models.TextField()
    experiences = models.ManyToManyField(Experience)
    education = models.ManyToManyField(Education)