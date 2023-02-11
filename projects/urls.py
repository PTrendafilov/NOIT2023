from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_job_page/', views.create_job_page, name='create_job_page'),
    path('create_project/', views.create_project, name='create_project'), 
    path('jobs_created_by_user/', views.jobs_created_by_user, name='jobs_created_by_user'), 
    path('project-detials/<int:id>', views.details_job, name='details_job'), 
    path('project-edit/<int:id>', views.project_edit, name='project_edit'), 
    path('project-delete/<int:id>', views.project_delete, name='project_delete'),
    path('aplly/<int:id>', views.aplly_for_job, name='aplly_for_job'),
    path('project-bids/<int:id>', views.project_bids, name='project_bids'),
]