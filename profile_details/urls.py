from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_page', views.create_page, name='create_page'),
    path('<int:id>', views.index, name='index'),
]