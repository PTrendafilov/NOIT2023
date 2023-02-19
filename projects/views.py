from django.shortcuts import render, redirect
from .models import *
import datetime
from accounts.models import Profile as User
import math
from django.http import HttpResponse

# Create your views here.
"""
This is a Python script using Django web framework. 
It defines various views that handle HTTP requests and return HTTP responses with HTML templates. 
Here is a brief explanation of each view:

1. get_time_from_creating: 
    This function takes a date object and calculates the time difference between the current time and the given date.
    It returns the time difference in a human-readable format (e.g., "2 days ago").

2. index: 
    This view retrieves all Project objects from the database,
    sorts them by the date they were created,
    and renders a template with the list of projects.

3. create_job_page:
     This view renders a template for creating a new job.

4. create_project:
     This view creates a new Project object based on the POST data received from the create job form and saves it to the database.

5. details_job:    
    This view retrieves the Project object with the given id from the database and renders a template with its details.

6.project_delete: 
    This view deletes the Project object with the given id from the database.

7. project_edit_page: 
    This view retrieves the Project object with the given id from the database and renders a template for editing it.

8. edit_project: 
    This view updates the Project object with the given id based on the POST data received from the edit job form and saves it to the database.
"""
def does_user_is_creator_project(user, project):
    if user != project.creator:
        return HttpResponse('You are not authorized to access this page.')
def does_user_is_creator_bid(user,application):
    if user != application.candidate:
        return HttpResponse('You are not authorized to access this page.')
def get_time_from_creating(date):
    current_date = datetime.datetime.now()
    if date.tzinfo is not None:
        date = date.replace(tzinfo=None)
    difference = current_date - date
    difference = difference.total_seconds()
    difference-=7200
    unit = 'seconds'
    if difference>60:
        difference/=60
        unit = 'minutes'
    if difference>60 and unit=='minutes':
        difference/=60
        unit = 'hours'
    if difference>24 and unit=='hours':
        difference/=24
        unit = 'days'
    if difference>7 and unit=='days':
        difference/=7
        unit = 'weeks'
    if math.floor(difference)==1:
        unit = unit[:-1]
    if unit=='seconds':
        unit = 'секунди'
    elif unit=='minutes':
        unit = 'минути'
    elif unit=='hours':
        unit = 'часа'
    elif unit=='days':
        unit = 'дни'
    elif unit=='weeks':
        unit = 'седмици'
    elif unit=='second':
       unit = 'секундa' 
    elif unit == 'minute':
        unit='минута'
    elif unit=='hour':
        unit = 'час'
    elif unit == 'day':
        unit = 'ден'
    elif unit == 'week':
        unit = 'седмица'
    return str(math.floor(difference)), unit
def index(request):
    jobs = Project.objects.all().order_by('-date_created')
    jobs_list = []
    for job in jobs:
        if job.is_it_done==False:
            job.time_from_creating = " ".join(get_time_from_creating(job.date_created))
            jobs_list.append(job)
            job.skills = job.skills.split('(*)')
    #current_date = datetime.datetime.now()
    return render(request, 'jobs-reading-page.html',{'jobs':jobs_list})

def create_job_page(request):
    return render(request, 'create.html')

def create_project(request):
    project = Project()
    project.name = request.POST['title']
    project.description = request.POST['description']
    project.skills = request.POST['skills']
    project.responsibilities = request.POST['responsibilities']
    currency_symbol = '$'
    if request.POST['payment-type']=='payment-for-hour':
        if request.POST['currency-hour']=='EUR-hour':
            currency_symbol = '€'
        if request.POST['currency-hour']=='USD-hour':
            currency_symbol = '$'
        if request.POST['currency-hour']=='BGN-hour':
            currency_symbol = 'LV'
        project.payment = request.POST['payment-hour'] + currency_symbol + '/h'
    if request.POST['payment-type']=='payment-for-project':
        if request.POST['currency-project']=='eur-project':
            currency_symbol = '€'
        if request.POST['currency-project']=='USD-project':
            currency_symbol = '$'
        if request.POST['currency-project']=='BGN-project':
            currency_symbol = 'LV'
        project.payment = request.POST['payment-project'] + currency_symbol
    #print(project.payment)
    project.creator = User.objects.get(username=request.user.username)
    project.save()
    return redirect(jobs_created_by_user)

def details_job(request, id):
    project=Project.objects.get(id=id)
    project.time_from_creating = " ".join(get_time_from_creating(project.date_created))
    flag=request.user.username==project.creator.username
    is_freelancer = False
    if request.user.is_authenticated:
        is_freelancer=request.user.role=='freelancer' or request.user.role=='teamleader'
    else:
        is_freelancer=False
    #print(is_freelancer)
    project.responsibilities = project.responsibilities.split('(*)')
    project.skills = project.skills.split('(*)')
    already_made_offer = False
    user = request.user
    if request.user.is_authenticated:
        if Application.objects.filter(candidate=user, apllications__id=id).exists():
            already_made_offer=True
    return render(request, 'job-details.html', {'project':project, 'flag':flag, 'is_freelancer':is_freelancer, 'already_made_offer': already_made_offer})

def project_delete(request, id):
    project = Project.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.')
    project.delete()
    return redirect(jobs_created_by_user)

def project_edit_page(request, id):
    project=Project.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.')
    project.skills = project.skills.split('(*)')
    project.responsibilities = project.responsibilities.split('(*)')
    project.payment_per_hour_flag = 0
    payment_value = ''
    for symbol in project.payment:
        if symbol>='0' and symbol<='9':
            payment_value+=symbol
    project.payment_value = payment_value
    for symbol in project.payment:
        if symbol=='h':
            project.payment_per_hour_flag=1
    for symbol in project.payment:
        if symbol == '$':
            project.currency = '$'
        if symbol == '€':
            project.currency = '€'
        if symbol == 'L':
            project.currency = 'LV'
    return render(request, 'edit-project.html', {'project':project})

def edit_project(request, id):
    project=Project.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.')
    project.name = request.POST['title']
    project.description = request.POST['description']
    project.skills = request.POST['skills']
    project.responsibilities = request.POST['responsibilities']
    currency_symbol = '$'
    if request.POST['payment-type']=='payment-for-hour':
        if request.POST['currency-hour']=='EUR':
            currency_symbol = '€'
        if request.POST['currency-hour']=='USD':
            currency_symbol = '$'
        if request.POST['currency-hour']=='BGN':
            currency_symbol = 'LV'
        project.payment = request.POST['payment-hour'] + currency_symbol + '/h'
    if request.POST['payment-type']=='payment-for-project':
        if request.POST['currency-project']=='EUR':
            currency_symbol = '€'
        if request.POST['currency-project']=='USD':
            currency_symbol = '$'
        if request.POST['currency-project']=='BGN':
            currency_symbol = 'LV'
        project.payment = request.POST['payment-project'] + currency_symbol
    project.creator = User.objects.get(username=request.user.username)
    project.save()
    #print(project.responsibilities)
    return redirect(jobs_created_by_user)

def aplly_for_job(request, id):
    project=Project.objects.get(id=id)
    apllication=Application()
    if request.POST['currency']=='EUR':
        currency_symbol = '€'
    if request.POST['currency']=='USD':
        currency_symbol = '$'
    if request.POST['currency']=='BGN':
        currency_symbol = 'LV'
    apllication.bid = request.POST['bid'] + currency_symbol
    apllication.cover_letter = request.POST['cover-letter']
    apllication.candidate =request.user
    #project.candidates.add(request.user)
    apllication.save()
    project.applications.add(apllication)
    project.bids = project.applications.count()
    project.save()
    return redirect(index)


def jobs_created_by_user(request):
    if request.user.role == 'client':
        projects_created_by_user = Project.objects.filter(creator=User.objects.get(username=request.user.username)).order_by('-date_created')
    jobs_list = []
    for job in projects_created_by_user:
        job.time_from_creating = " ".join(get_time_from_creating(job.date_created))
        jobs_list.append(job)
        job.skills = job.skills.split('(*)')
    done_job_list = []
    paid_done_jobs_list = []
    undone_job_list = []
    for job in projects_created_by_user:
        if job.is_it_done and not job.is_it_paid:
            done_job_list.append(job)
            #print(job.name)
        elif job.is_it_done and job.is_it_paid:
            paid_done_jobs_list.append(job)
        else:
            undone_job_list.append(job)
    return render(request, 'profile-created-jobs.html', {'user_jobs':jobs_list, 'done_jobs':done_job_list, 'undone_jobs':undone_job_list,'paid_jobs':paid_done_jobs_list})


def project_bids(request, id):
    project = Project.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.')
    applications = project.applications.all()
    applications_list = []
    flag = False
    accepted_bid = None
    for application in applications:
        application.time_from_creating = " ".join(get_time_from_creating(application.date_created))
    for application in applications:
        if application.is_accepted == True :
            accepted_bid = application
            flag = True
        elif not application.is_rejected:
            applications_list.append(application)
    return render(request, 'bids-reading-page.html', {'applications':applications_list, 'project':project, 'accepted_bid': accepted_bid, 'flag_accepted_bid': flag})


def accept_bid(request, id):
    application = Application.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.')
    application.is_accepted = True
    project = application.apllications.all()[0]
    project_id = project.id
    application.save()
    return redirect('project_bids', id=project_id)

def reject_bid(request, id):
    application = Application.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.') 
    project = application.apllications.all()[0]
    project_id = project.id
    application.is_rejected = True
    application.save()
    return redirect('project_bids', id=project_id)

def project_is_done(request, id):
    project = Project.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.')
    applications = project.applications.all()
    project.is_it_done = True
    for application in applications:
        if application.is_accepted == True :
            user = application.candidate
            user.points+=1
            user.save()
    project.save()
    return redirect(jobs_created_by_user)

def remove_accepted_bid(request, id):
    application = Application.objects.get(id=id)
    if request.user != project.creator:
        return HttpResponse('You are not authorized to access this page.')    
    project = application.apllications.all()[0]
    project_id = project.id
    application.is_rejected = True
    application.is_accepted = False
    application.save()
    return redirect('project_bids', id=project_id)

def bids_made_by_user(request):
    applications = request.user.candidate.all()
    rejected_bids = []
    accepted_bids = []
    waiting_bids = []
    done_bids = []
    paid_bids = []
    for application in applications:
        application.time_from_creating = " ".join(get_time_from_creating(application.date_created))
        project = application.apllications.all()[0]
        application.project = project
        if application.is_rejected == True:
            rejected_bids.append(application)
            #print('Hello')
        if application.is_accepted == True and project.is_it_done==False:
            accepted_bids.append(application)
        if application.is_accepted == True and project.is_it_done==True and project.is_it_paid==False:
            done_bids.append(application)
        if application.is_accepted == True and project.is_it_done==True and project.is_it_paid==True:
            paid_bids.append(application)
        if not application.is_rejected and not application.is_accepted:
            waiting_bids.append(application)
    if applications:
        project = applications[0].apllications.all()[0]
    else:
        project=None

    return render(request, 'profile-created-bids.html', {'user_applications':applications, 'project':project, 'accepted_bids':accepted_bids, 'rejected_bids':rejected_bids, 'waiting_bids':waiting_bids, 'done_bids':done_bids, 'paid_bids':paid_bids})

def delete_bid(request, id):
    application = Application.objects.get(id=id)
    if request.user != application.candidate:
        return HttpResponse('You are not authorized to access this page.')
    project = application.apllications.all()[0]
    project.bids -= 1
    project.save()
    application.delete()
    return redirect('bids_made_by_user')

def verify_payment(request, id):
    project = Project.objects.get(id=id)
    project.is_it_paid = True
    project.save()
    return redirect('bids_made_by_user')