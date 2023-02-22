from django.shortcuts import render
from .models import CV
from accounts.models import Profile as User
# Create your views here.
def index(request,id):
    content = {}
    return render(request, 'profile-details-page.html')
def create_page(request):
    return render(request, 'create-profile-details.html')