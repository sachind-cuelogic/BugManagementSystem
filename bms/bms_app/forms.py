from django import forms
from django.forms import ModelForm
from .models import Product_type
from .models import ProductDetails
from .models import ProductUser
from django.contrib.auth.models import User

class User_info_form(ModelForm):
	class Meta:
		model = User
		fields = ("username","email","password")

class Product_type_form(ModelForm):
	class Meta:
		model = Product_type
		fields = ('product_type_name',)
