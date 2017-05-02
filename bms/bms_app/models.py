from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class ProjectType(models.Model):
    project_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.project_type_name

class ProductDetails(models.Model):
    prod_name = models.CharField(max_length=50)
    prod_type = models.ForeignKey(ProjectType)
    prod_version = models.CharField(max_length=50, null=True, blank=True)
    prod_description = models.CharField(max_length=1000, null=True, blank=True)
    prod_file = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

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
        return u'{0}'.format(self.prod_user_role)

class BugType(models.Model):
    bug_name = models.CharField(max_length=50)

    def __str__(self):
        return self.bug_name

class BugStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name

class BugDetails(models.Model):
    project_name = models.ForeignKey(ProductDetails)
    title = models.CharField(max_length=50)
    bug_type = models.ForeignKey(BugType)
    status = models.ForeignKey(BugStatus)
    build_version = models.CharField(max_length=50)
    sprint_no = models.CharField(max_length=50)
    dependent_module = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=1000)
    bug_owner = models.ForeignKey(User, related_name='bug_owner')
    bug_assigned_to = models.ForeignKey(User, related_name='bug_assigned_to')
    bug_file = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.comment
        