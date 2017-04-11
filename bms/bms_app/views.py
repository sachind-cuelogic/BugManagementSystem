import json
import os
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django import forms
from .forms import User_inof_form
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product_type, ProductDetails, UserRole, ProductUser

def home(request):
    return render(request, 'bms_app/home.html')

def register(request):
    if request.method == 'POST':
        form = User_inof_form(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']


            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                user.save()
                emaill = EmailMessage('Registration Confirmation for Bug Management System', 'Dear ' + username +
                                      ',\n\nThank you for registering to Bug Managment System.  We have good features the can help you to the management of the bugs which are as follows:\nAuthentication and Authorization, Products, Bug, Attachment, Admin, Users, Configuration, Log View, Search & View, Comments and tagging.\n\nLogin: https://www.facebook.com/ybts.ybts.9  \n\nIf you have any questions please contact: bug.system.app1@gmail.com. \n\nThank you,\nBug Management System.', to=[user.email])
                emaill.send()
                messages.success(request, "You have successfully registered!")
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'bms_app/register.html')
                messages.warning(
                    request, "Looks like a username with that email already exists!")

    else:
        form = User_inof_form()

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
def create_product(request):
    if request.method == 'GET':
        users = User.objects.filter()
        roles = UserRole.objects.filter()
        prod_types = Product_type.objects.filter()
        return render(request, 'registration/create_product.html', {'users': users, 'roles': roles, 'prod_types': prod_types})
    else:
        data = request.POST
        data1 = request.FILES

        list1 = data['user_data']
        ptype = data['ptype']
        save_prod_detail = ProductDetails(prod_name=data['prod_name'],
                                          prod_type_id=int(ptype),
                                          prod_version=data['prod_version'],
                                          prod_description=data[
                                              'prod_description'],
                                          prod_file=data1['prod_file'])

        save_prod_detail.save()

        for each in json.loads(list1):
            save_prod_user = ProductUser(prod_user_id=int(
                each['user_id']), prod_user_role_id=int(each['user_role']))

        save_prod_user.save()
        return HttpResponse(json.dumps({'success': True}), 
                            content_type="application/json")


@login_required(login_url='/login/')
def product_list(request):
    return render(request, 'registration/product_list.html')


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
