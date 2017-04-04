import json
import os
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import User_inof_form
from .forms import ProductDetailsForm, ProductUserForm
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product_type, ProductDetails, UserRole,ProductUser
from django.forms.formsets import formset_factory
# from jfu.http import upload_receive, UploadResponse, JFUResponse
# from django.core.urlresolvers import reverse
# from django.views import generic
# from django.views.decorators.http import require_POST



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
                #form.save()
                emaill = EmailMessage('Registration Confirmation for Bug Management System'
                    ,'Dear '+ username+',\n\nThank you for registering to Bug Managment System.  We have good features the can help you to the management of the bugs which are as follows:\nAuthentication and Authorization, Products, Bug, Attachment, Admin, Users, Configuration, Log View, Search & View, Comments and tagging.\n\nLogin: http://127.0.0.1:8000/login/  \n\nIf you have any questions please contact: bug.system.app1@gmail.com. \n\nThank you,\nBug Management System.'
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
        prod_types =Product_type.objects.filter() 
        return render(request, 'registration/create_product.html', {'users':users,'roles':roles,'prod_types':prod_types})
    else:
        # import pdb
        # pdb.set_trace()
        data = request.POST
        prod_desc =  data['prod_desc']
        prod_name = data['prod_name'] 
        prod_type = data['prod_type']
        prod_ver = data['prod_ver']
        prod_file = data['prod_file']
        # user_data = data['prod_user_data']

        u= ProductDetails.objects.create(prod_name=prod_name,prod_version=prod_ver,prod_description=prod_desc,prod_type=prod_type)
        u.save()
        #return HttpResponse(json.dumps({'response':""+user1.username+":"+user2.role}), content_type="application/json")


@login_required(login_url='/login/')
def product_list(request):
    return render(request, 'registration/product_list.html')  
            
# @require_POST
# def upload(request):
#     file = upload_receive(request)
#     instance = ProductDetails( prod_file = file )
#     instance.save()
#     basename = os.path.basename( instance.file.path )

#     file_dict = {
#         'name' : basename,
#         'size' : file.size,

#         'url': settings.MEDIA_URL + basename,
#         'thumbnailUrl': settings.MEDIA_URL + basename,

#         'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
#         'deleteType': 'POST',
#     }

#     return UploadResponse( request, file_dict )
