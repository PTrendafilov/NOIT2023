from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import Profile as User
from django.http import HttpResponse, HttpResponseForbidden
from .get_time import *
#########################################
############   DECORATORS   #############
#########################################
def client_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'client':
            return HttpResponseForbidden('You have no permissions')
        return view_func(request,*args, **kwargs)
    return wrapper

def project_creator_required(view_func):
    def wrapper(request, id,*args, **kwargs):
        user = request.user
        project = get_object_or_404(Project, id=id)
        if project.creator != request.user:
            return HttpResponseForbidden('You have no permissions')
        return view_func(request, id,*args, **kwargs)
    return wrapper

def freelancer_required(view_func):
    def wrapper(request,*args, **kwargs):
        if request.user.role != 'freelancer':
            return HttpResponseForbidden('You have no permissions')
        return view_func(request,*args, **kwargs)
    return wrapper


#########################################
##########   MAIN FUNCTIONS   ###########
#########################################
def index(request):
    jobs = Project.objects.all().order_by('-date_created')
    jobs_list = []
    for job in jobs:
        if job.is_it_done==False:
            job.time_from_creating = " ".join(get_time_from_creating(job.date_created))
            jobs_list.append(job)
            job.skills = job.skills.split('(*)')
    return render(request, 'jobs-reading-page.html',{'jobs':jobs_list})

def jobs_created_by_user(request):
    if request.user.role == 'client':
        projects_created_by_user = Project.objects.filter(creator=request.user).order_by('-date_created')
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
        elif job.is_it_done and job.is_it_paid:
            paid_done_jobs_list.append(job)
        else:
            undone_job_list.append(job)
    return render(request, 'profile-created-jobs.html', {'user_jobs':jobs_list, 'done_jobs':done_job_list, 'undone_jobs':undone_job_list,'paid_jobs':paid_done_jobs_list})

@client_required
def create_job_page(request):
    return render(request, 'create.html')

@client_required
def create_project(request):
    project = Project()
    project.name = request.POST['title']
    project.description = request.POST['description']
    project.skills = request.POST['skills']
    project.responsibilities = request.POST['responsibilities']
    if request.POST['payment-type']=='payment-for-hour':
        project.currency = request.POST['currency-hour']
        project.payment = request.POST['payment-hour']
        project.payment_type_hourly = True
    else:
        project.currency = request.POST['currency-project']
        project.payment = request.POST['payment-project']
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
    project.responsibilities = project.responsibilities.split('(*)')
    project.skills = project.skills.split('(*)')
    already_made_offer = False
    if request.user.is_authenticated:
        if Application.objects.filter(project=project, candidate=request.user).exists():
            already_made_offer=True
    return render(request, 'job-details.html', {'project':project, 'flag':flag, 'is_freelancer':is_freelancer, 'already_made_offer': already_made_offer})

@project_creator_required
def project_delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect(jobs_created_by_user)

@project_creator_required
def project_edit_page(request, id):
    project=Project.objects.get(id=id)
    project.skills = project.skills.split('(*)')
    project.responsibilities = project.responsibilities.split('(*)')
    return render(request, 'edit-project.html', {'project':project})

@project_creator_required
def edit_project(request, id):
    project = Project.objects.get(id=id)
    project.name = request.POST['title']
    project.description = request.POST['description']
    project.skills = request.POST['skills']
    project.responsibilities = request.POST['responsibilities']
    if request.POST['payment-type']=='payment-for-hour':
        project.currency = request.POST['currency-hour']
        project.payment = request.POST['payment-hour']
        project.payment_type_hourly = True
    else:
        project.currency = request.POST['currency-project']
        project.payment = request.POST['payment-project']
    project.creator = User.objects.get(username=request.user.username)
    project.save()
    return redirect(jobs_created_by_user)

@freelancer_required
def aplly_for_job(request, id):
    project=Project.objects.get(id=id)
    apllication=Application()
    apllication.currency = request.POST['currency']
    apllication.bid = request.POST['bid']
    apllication.cover_letter = request.POST['cover-letter']
    apllication.candidate = request.user
    apllication.project = project
    apllication.save()
    project.bids += 1
    project.save()
    return redirect(index)

@project_creator_required
def project_bids(request, id):
    project = Project.objects.get(id=id)
    applications = Application.objects.filter(project=project)
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

@project_creator_required
def accept_bid(request, id):
    application = Application.objects.get(id=id)
    project = application.project
    application.is_accepted = True
    project_id = project.id
    application.save()
    return redirect('project_bids', id=project_id)

@project_creator_required
def reject_bid(request, id):
    application = Application.objects.get(id=id)
    project = application.project
    project_id = project.id
    application.is_rejected = True
    application.save()
    return redirect('project_bids', id=project_id)

@project_creator_required
def project_is_done(request, id):
    project = Project.objects.get(id=id)
    applications = Application.objects.filter(project=project)
    project.is_it_done = True
    for application in applications:
        if application.is_accepted == True :
            user = application.candidate
            user.points+=1
            user.save()
    project.save()
    return redirect(jobs_created_by_user)

@project_creator_required
def remove_accepted_bid(request, id):
    application = Application.objects.get(id=id)
    project = application.project
    project_id = project.id
    application.is_rejected = True
    application.is_accepted = False
    application.save()
    return redirect('project_bids', id=project_id)

@freelancer_required
def bids_made_by_user(request):
    applications = Application.objects.filter(candidate=request.user)
    rejected_bids = []
    accepted_bids = []
    waiting_bids = []
    done_bids = []
    paid_bids = []
    for application in applications:
        application.time_from_creating = " ".join(get_time_from_creating(application.date_created))
        project = application.project
        if application.is_rejected == True:
            rejected_bids.append(application)
        if application.is_accepted == True and project.is_it_done==False:
            accepted_bids.append(application)
        if application.is_accepted == True and project.is_it_done==True and project.is_it_paid==False:
            done_bids.append(application)
        if application.is_accepted == True and project.is_it_done==True and project.is_it_paid==True:
            paid_bids.append(application)
        if not application.is_rejected and not application.is_accepted:
            waiting_bids.append(application)
    return render(request, 'profile-created-bids.html', {'user_applications':applications, 'accepted_bids':accepted_bids, 'rejected_bids':rejected_bids, 'waiting_bids':waiting_bids, 'done_bids':done_bids, 'paid_bids':paid_bids})

@freelancer_required
def delete_bid(request, id):
    application = Application.objects.get(id=id)
    if request.user != application.candidate:
        return HttpResponse('You are not authorized to access this page.')
    project = application.project
    project.bids -= 1
    project.save()
    application.delete()
    return redirect('bids_made_by_user')

@freelancer_required
def verify_payment(request, id):
    project = Project.objects.get(id=id)
    project.is_it_paid = True
    project.save()
    return redirect('bids_made_by_user')