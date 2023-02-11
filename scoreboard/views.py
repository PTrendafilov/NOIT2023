from django.shortcuts import render
from accounts.models import Profile as User
# Create your views here.
def index(request):
    users = User.objects.all().order_by('-points')
    for user in users:
        print(user.username, user.points)
    return render(request, 'scoreboard.html', {'users':users})