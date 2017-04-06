from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import User_inof_form
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'bms_app/home.html')
    
@csrf_exempt
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
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username = username, password = password)
                login(request, user)
                form.save()
                user.save()
                emaill = EmailMessage('Hello','You have successfully registered.', to=[user.email])
                emaill.send()
                messages.success(request, "You have successfully registered!")
                return HttpResponseRedirect('/login')
            else:
                messages.warning(request, "Looks like a username with that email already exists!")
                return render(request, 'bms_app/register.html')
    else:
        form = User_inof_form()
    return render(request, 'bms_app/register.html', {'form' : form})

@login_required(login_url='/login/')
def product_home_page(request):
    return render(request, 'registration/home_page.html')
    