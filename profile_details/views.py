from django.shortcuts import render
from .models import CV
from accounts.models import Profile as User
# Create your views here.
def index(request):
    
    content = {}
    return render(request, 'profile-details-page.html')