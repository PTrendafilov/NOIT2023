from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_page', views.create_page, name='create_page'),
    path('create_cv/', views.create_cv, name='create_cv'),
    path('<str:username>/', views.index, name='index'),
    path('profile-edit-page/<str:username>/', views.profile_edit_page, name='profile_edit_page'),
    path('profile-edit/<str:username>/', views.profile_edit, name='profile_edit'),
    path('profile-delete/<str:username>/', views.profile_delete, name='profile_delete'),
    path('download-cv/<str:username>/', views.download_cv, name='download_cv'),
]