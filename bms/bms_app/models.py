from __future__ import unicode_literals
from django.db import models

class User_info(models.Model):
	username = models.CharField(max_length=50)
	email    = models.EmailField(unique=True, blank=False)
	password = models.CharField(max_length=50)
	designation = models.CharField(max_length=50,default="Software Engineer")
	is_active   = models.BooleanField(default=True)
	is_admin    = models.BooleanField(default=False)
	is_staff    = models.BooleanField(default=False)

	def __str__(self):
		return u'{0}'.format(self.username)

class Product_type(models.Model):
	product_type_name = models.CharField(max_length=50)

	def __str__(self):
		return u'{0}'.format(self.product_type_name)

class UserRole(models.Model):
	role = models.CharField(max_length=50)

	def __str__(self):
		return u'{0}'.format(self.role)

class ProductDetails(models.Model):
	prod_name = models.CharField(max_length=50)
	prod_type = models.ForeignKey(Product_type)
	prod_user = models.ForeignKey(User_info,null=True)
	user_role = models.ForeignKey(UserRole,null=True)
	prod_version = models.CharField(max_length=50,null=True)
	prod_description = models.CharField(max_length=1000,null=True)
	prod_file = models.FileField(upload_to='documents/%Y/%m/%d',null=True)
