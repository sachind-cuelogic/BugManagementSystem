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
