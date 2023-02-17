from django.shortcuts import render
from accounts.models import Profile as User
# Create your views here.
def index(request):
    users = User.objects.all().order_by('-points')
    counter = 0
    for i in range(len(users)):
        if users[i].role == 'freelancer':
            counter+=1
            users[i].place = counter
            print(users[i].username)
        #print(user.username, user.points)
    return render(request, 'scoreboard.html', {'users':users})