import json
import os
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django import forms
from .forms import User_info_form
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProjectType, ProductDetails, UserRole, ProductUser, BugType, BugStatus
from .models import BugDetails
from .forms import Bug_Details_Form


def home(request):
    return render(request, 'bms_app/home.html')

def register(request):
    if request.method == 'POST':
        form = User_info_form(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                user.save()
                emaill = EmailMessage('Registration Confirmation for Bug Management System', 
                                        'Dear ' + username +
                                      ',\n\nThank you for registering to Bug Managment System. '
                                      ' We have good features the can help you to the management '
                                      'of the bugs which are as follows:\nAuthentication and Authorization,'
                                      ' Products, Bug, Attachment, Admin, Users, Configuration, Log View, Search & View, '
                                      'Comments and tagging.\n\nLogin: https://www.facebook.com/ybts.ybts.9  '
                                      '\n\nIf you have any questions please contact: bug.system.app1@gmail.com.'
                                      ' \n\nThank you,\nBug Management System.', to=[user.email])
                emaill.send()
                messages.success(request, "You have successfully registered!")
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'bms_app/register.html')
                messages.warning(
                    request, "Looks like a username with that email already exists!")

    else:
        form = User_info_form()

    return render(request, 'bms_app/register.html', {'form': form})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/website_home')
    else:
        return HttpResponse("invalid login")


def website_home(request):
    return render(request, 'registration/website_home.html')

@login_required(login_url='/login/')
def create_project(request):

    if request.method == 'GET':
        users = User.objects.all()
        roles = UserRole.objects.all()
        prod_types = ProjectType.objects.all()

        return render(request, 'registration/create_project.html', 
            {'users': users, 'roles': roles, 'prod_types': prod_types})
    else:
        data = request.POST
        data1 = request.FILES
        if request.FILES:
            data1['prod_file'] = request.FILES['prod_file']
        else:
            data1['prod_file'] = ""
        
        list1 = data['user_data']
        ptype = data['ptype']
        save_prod_detail = ProductDetails(prod_name=data['prod_name'],
                                          prod_type_id=int(ptype),
                                          prod_version=data['prod_version'],
                                          prod_description=data[
                                              'prod_description'],
                                          prod_file=data1['prod_file'])

        save_prod_detail.save()

        product_id = save_prod_detail.id

        for each in json.loads(list1):
            save_prod_user = ProductUser(prod_user_id=int(
                            each['user_id']), 
                            prod_user_role_id=int(each['user_role']),
                            product_id=product_id)
            save_prod_user.save()

        
        return HttpResponse(json.dumps({'success': True}), 
                            content_type="application/json")

@login_required(login_url='/login/')
def project_list(request):
    if request.user.is_authenticated():
        current_user = request.user
        user_list = ProductUser.objects.raw("SELECT "
            "pu.id, count(bd.id) as bugcount, pd.prod_name, pd.prod_version, ur.role, pd.id as product_id,(select count(id) from bms_app_bugdetails where status_id <> 22 and project_name_id = pd.id) as openbug "
            "FROM bms_app_productuser pu "
            "JOIN bms_app_productdetails pd ON pd.id = pu.product_id "
            "JOIN bms_app_userrole ur ON ur.id = pu.prod_user_role_id "
            "LEFT JOIN bms_app_bugdetails bd ON bd.project_name_id = pd.id "
            "where pu.prod_user_id = %s "
            "GROUP BY pu.id, pd.prod_name, pd.prod_version, ur.role, pd.id", [current_user.id])

        messages.success(request, "You have successfully created project!")
        return render(request, 'registration/project_list.html', 
                        {'user_list': list(user_list)})

    return render(request, 'registration/project_list.html')

@login_required(login_url='/login/')
def create_bug(request):
    if request.user.is_authenticated():
        current_user = request.user
    if request.method == 'GET':
        project_name = ProductUser.objects.all().filter(prod_user_id = current_user.id)
        bug_type = BugType.objects.all()
        status = BugStatus.objects.all()
        bug_owner = User.objects.all()
        bug_assign = User.objects.all()
        return render(request, 'registration/create_bug.html', 
            {'project_name': project_name,'bug_type':bug_type,'status':status,
            'bug_owner':bug_owner,'bug_assign':bug_assign})

    if request.method == 'POST':
        bug_form = Bug_Details_Form(request.POST, request.FILES)
        if bug_form.is_valid():
            userObj = bug_form.cleaned_data
            bug_form.save()
            messages.success(request, "You have successfully created bug!")
            return HttpResponseRedirect('/bug_view/')    
    else:
        bug_form = Bug_Details_Form()

    return render(request, 'registration/create_bug.html', 
                    {'bug_form' : bug_form})

def bug_view(request):
    return render(request, 'registration/bug_view.html')

def services(request):
    return render(request, 'registration/services.html')

def about(request):
    return render(request, 'registration/about.html')

def contact_us(request):
    return render(request, 'registration/contact.html')

def privacy(request):
    return render(request, 'registration/privacy.html')

def terms_use(request):
    return render(request, 'registration/terms_use.html')

def header_sidebar(request):
    return render(request, 'registration/header_sidebar.html')

def landing_header_footer(request):
    return render(request, 'registration/landing_header_footer.html')