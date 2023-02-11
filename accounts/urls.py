from django.urls import path

from . import views

urlpatterns = [
    # Index page
    path('', views.index, name='index'),
    # Login function
    path('login', views.login, name='login'),
    # Login form page
    path('login_page', views.login_page, name='login_page'),
    # Registration form page
    path('registration_page', views.registration_page, name='registration_page'),
    # Processes the registration of a user
    path('registrate_user', views.registrate_user, name='registrate_user'),
    # Logout function
    path('logout/', views.logout_page, name='logout_page'),
    # Page for selecting user role
    path('choose_role', views.choose_role, name='choose_role'),
]