from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Product_type(models.Model):
	product_type_name = models.CharField(max_length=50)

	def __str__(self):
		return self.product_type_name

class ProductDetails(models.Model):
	prod_name = models.CharField(max_length=50)
	prod_type = models.ForeignKey(Product_type)
	prod_version = models.CharField(max_length=50,null=True)
	prod_description = models.CharField(max_length=1000,null=True)
	prod_file = models.FileField(upload_to='documents/%Y/%m/%d',null=True)

	def __str__(self):
		return self.prod_name

class UserRole(models.Model):
	role = models.CharField(max_length=50)
	def __str__(self):
		return self.role

class ProductUser(models.Model):

	prod_user = models.ForeignKey(User, null=True)
	product = models.ForeignKey(ProductDetails, null=True)
	prod_user_role = models.ForeignKey(UserRole)

	def __str__(self):
		return self.prod_user_role

	def __str__(self):
		return u'{0}'.format(self.prod_user_role)
