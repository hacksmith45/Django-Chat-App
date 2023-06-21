from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    
    # Retrieve the unique users from the messages
    users = User.objects.filter(messages__in=messages).distinct()
    
    
    return render(request, 'room/room.html', {'room': room, 'messages': messages, 'users':users})