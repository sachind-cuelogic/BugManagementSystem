from django.conf.urls import url
from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register
from .views import create_product
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^create_product/',views.create_product),
    #url(r'^create_product/',views.upload,name = 'jfu_upload'),
    url(r'^website_home/',views.website_home),
    url(r'^product_list/',views.product_list),
    url(r'^logout/', auth_views.logout),
  #  url(r'^sample_url/', views.get_sample_data),
]
