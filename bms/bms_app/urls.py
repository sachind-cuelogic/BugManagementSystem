from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register
from .views import create_project
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', views.register, name="register"),
    url(r'^login/', auth_views.login,name="login"),
    url(r'^create_project/', views.create_project),
    url(r'^website_home/', views.website_home),
    url(r'^project_list/', views.project_list),
    url(r'^create_bug/', views.create_bug, name="create_bug"),
    url(r'^bug_list/', views.bug_list),
    url(r'^logout/', auth_views.logout),
    url(r'^services/', views.services),
    url(r'^about/', views.about),
    url(r'^contact/', views.contact_us),
    url(r'^privacy/', views.privacy),
    url(r'^terms_use/', views.terms_use),
    url(r'^header_sidebar/', views.header_sidebar),
    url(r'^landing_header_footer/', views.landing_header_footer),
    url(r'^bug_list/(?P<pid>[0-9]+)/$', views.bug_list, 
                                                name="bug_list")
]
