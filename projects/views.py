from django.shortcuts import render, redirect
from .models import *
import datetime
from accounts.models import Profile as User
import math
# Create your views here.
def get_time_from_creating(date):
    current_date = datetime.datetime.now()
    if date.tzinfo is not None:
        date = date.replace(tzinfo=None)
    difference = current_date - date
    difference = difference.total_seconds()
    difference-= 7200
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
    return str(math.floor(difference)), unit
def index(request):
    jobs = Project.objects.all().order_by('-date_created')
    jobs_list = []
    for job in jobs:
        job.time_from_creating = " ".join(get_time_from_creating(job.date_created))
        jobs_list.append(job)
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
    if request.POST['currency']=='EUR':
        currency_symbol = '€'
    if request.POST['currency']=='USD':
        currency_symbol = '$'
    if request.POST['currency']=='BGN':
        currency_symbol = 'LV'
    if request.POST['payment-type']=='payment-for-hour':
        project.payment = request.POST['payment-hour'] + currency_symbol + '/h'
    if request.POST['payment-type']=='payment-for-project':
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
    return render(request, 'job-details.html', {'project':project, 'flag':flag, 'is_freelancer':is_freelancer})
def project_delete(request, id):
    Project.objects.get(id=id).delete()
    return redirect(jobs_created_by_user)
def project_edit(request, id):
    pass

def aplly_for_job(request, id):
    project=Project.objects.get(id=id)
    project.bids+=1
    apllication=Application()
    apllication.bid = request.POST['bid']
    apllication.cover_letter = request.POST['cover-letter']
    apllication.candidate =request.user
    #project.candidates.add(request.user)
    apllication.save()
    project.applications.add(apllication)
    project.save()
    return redirect(index)


def jobs_created_by_user(request):
    if request.user.role == 'client':
        projects_created_by_user = Project.objects.filter(creator=User.objects.get(username=request.user.username)).order_by('-date_created')
    jobs_list = []
    for job in projects_created_by_user:
        job.time_from_creating = " ".join(get_time_from_creating(job.date_created))
        jobs_list.append(job)
    return render(request, 'profile-created-jobs.html', {'user_jobs':jobs_list})


def project_bids():
    pass