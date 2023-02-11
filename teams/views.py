from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'team-viz.html')
def create_team(request):
    return render(request, 'team-creation.html')