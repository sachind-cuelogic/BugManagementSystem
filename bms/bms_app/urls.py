from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register
from .views import create_product
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', views.register, name="register"),
    url(r'^login/', auth_views.login,name="login"),
    url(r'^create_product/', views.create_product),
    url(r'^website_home/', views.website_home),
    url(r'^product_list/', views.product_list),
    url(r'^logout/', auth_views.logout),
    url(r'^services/', views.services),
    url(r'^about/', views.about),
    url(r'^contact/', views.contact_us),
    url(r'^privacy/', views.privacy),
    url(r'^terms_use/', views.terms_use),
]
