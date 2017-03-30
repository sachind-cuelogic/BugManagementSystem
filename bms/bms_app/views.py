from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import User_inof_form
from .forms import ProductDetailsForm
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_info, Product_type, ProductDetails

def home(request):
    return render(request, 'bms_app/home.html')

def register(request):
    if request.method == 'POST':
        form = User_inof_form(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                user.save()
                form.save()
                emaill = EmailMessage('Registration Confirmation for Bug Management System'
                    ,'Dear '+ username+',\n\nThank you for registering to Bug Managment System.  We have good features the can help you to the management of the bugs as follows:\nAuthentication and Authorization, Products, Bug, Attachment, Admin, Users, Configuration, Log View, Search & View, Comments and tagging.\n\nLogin: http://127.0.0.1:8000/login/  \n\nIf you have any questions please contact: bug.system.app1@gmail.com. \n\nThank you,\nBug Management System.'
                    , to=[user.email])
                emaill.send()
                messages.success(request, "You have successfully registered!")
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'bms_app/register.html')
                messages.warning(request, "Looks like a username with that email already exists!")
                
    else:
        form = User_inof_form()

    return render(request, 'bms_app/register.html', {'form' : form})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render_to_response('registration/create_product.html')
        
    else:
        return HttpResponse("invalid login")

def website_home(request):
    return render(request, 'registration/website_home.html')

@login_required(login_url='/login/')
def create_product(request):
    if request.method == 'POST':
        form = ProductDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            userObj = form.cleaned_data
            form.save()
            return HttpResponseRedirect('/product_list/')    
    else:
        form = ProductDetailsForm()

    return render(request, 'registration/create_product.html', {'form' : form})

@login_required(login_url='/login/')
def product_list(request):
    return render(request, 'registration/product_list.html')
