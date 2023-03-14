from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *
from .get_time import *
from django.http import HttpResponse, HttpResponseForbidden
# Create your views here.

def index(request):
    rooms = Room.objects.filter()
    for room in rooms:
        all_messages = Message.objects.filter(room=room)
        room.last_message = all_messages[len(all_messages)-1]
        room.last_message_time = " ".join(get_time_from_creating(room.last_message.date_created))
    user = request.user
    context = {}
    user_rooms = []
    for room in rooms:
        if user in room.users.all():
            user_rooms.append(room)
    context = {'rooms':user_rooms}
    return render(request, 'chat.html', context)