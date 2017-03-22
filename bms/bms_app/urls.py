from django.conf.urls import url

from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register
from .views import product_home_page
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^home_page/',views.product_home_page),
    url(r'^logout/', auth_views.logout),
]
