from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import Profile as User
"""
The provided code defines several views for a Django-based web application, related to user registration, login, and logout functionality.

choose_role: returns a form for choosing a role.
index: returns a login form.
registration_page: returns a registration form with a selected role passed as a context variable.
registrate_user: creates a new user based on the POST data and redirects to the login page.
login: authenticates a user based on email and password, logs them in if authentication is successful and redirects to a projects page.
login_page: returns a login form.
logout_page: logs out a user and redirects to the index page.

"""
def choose_role(request):
    return render(request, 'choose-role-form.html')
def index(request):
    return render(request, 'login.html')
def registration_page(request):
    selected_role = request.POST['role']
    print(selected_role)
    selected_role = selected_role
    return render(request, 'registration.html', {'selected_role': selected_role, 'selected_role_capitalize': selected_role.capitalize()})
def registrate_user(request):
    email = request.POST['email']
    username = request.POST['username']
    last_name = request.POST['last_name']
    first_name = request.POST['first_name']
    password = request.POST['password']
    role = request.POST['role']
    if role=='ментор':
        role = 'teamleader'
    if role=='ученик':
        role = 'freelancer'
    if role=='бизнес':
        role = 'client'
    user =  User.objects.create_user(first_name = first_name, password = password, last_name = last_name, email=email, username=username, role=role)
    return redirect(login_page)
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    username = User.objects.get(email=email.lower()).username
    user = authenticate(username = username, password = password)
    #print(user)
    if user is not None:
        auth_login(request, user)
        return redirect('/projects')
    else:
        return HttpResponse('Error')
def login_page(request):
    return render(request, 'login.html')
def logout_page(request):
    auth_logout(request)
    return redirect(index)