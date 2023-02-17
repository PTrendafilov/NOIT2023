from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_job_page/', views.create_job_page, name='create_job_page'),
    path('create_project/', views.create_project, name='create_project'), 
    path('jobs_created_by_user/', views.jobs_created_by_user, name='jobs_created_by_user'), 
    path('project-detials/<int:id>', views.details_job, name='details_job'), 
    path('project-edit/<int:id>', views.project_edit_page, name='project_edit_page'), 
    path('project-delete/<int:id>', views.project_delete, name='project_delete'),
    path('aplly/<int:id>', views.aplly_for_job, name='aplly_for_job'),
    path('project-bids/<int:id>', views.project_bids, name='project_bids'),
    path('accept/<int:id>', views.accept_bid, name='accept_bid'),
    path('reject/<int:id>', views.reject_bid, name='reject_bid'),
    path('project_is_done/<int:id>', views.project_is_done, name='project_is_done'),
    path('remove_accepted_bid/<int:id>', views.remove_accepted_bid, name='remove_accepted_bid'),
    path('delete_bid/<int:id>', views.delete_bid, name='delete_bid'),
    path('verify_payment/<int:id>', views.verify_payment, name='verify_payment'),
    path('bids_made_by_user/', views.bids_made_by_user, name='bids_made_by_user'),
]