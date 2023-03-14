from django.db import models

from accounts.models import Profile as User
# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=None)
    date_created = models.DateTimeField(auto_now_add=True)  # new field
    def __str__(self):
        return f'{self.text}'