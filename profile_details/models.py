from django.db import models
from accounts.models import Profile as User

class CV(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    about_me = models.TextField()
    skills = models.TextField()
    file = models.FileField(upload_to='CV/')
    def __str__(self):
        return f'{self.user.username} CV'