from django.test import TestCase
import unittest
import os
import string
from django.core.mail import EmailMessage
import re
from django.contrib.auth.models import User
from .forms import ProductDetailsForm

class Testpass(unittest.TestCase):
	def test_pass1_pass2(self):
		pass1=os.environ.get('pass1')
		pass2=os.environ.get('pass2')
		self.assertEqual(pass1,pass2)	
		self.assertNotEqual(pass1,pass2)

	def test_pass_len(self):
	 	passwd = os.environ.get('passlen')
	 	self.assertGreater(len(passwd),8)
		self.assertLess(len(passwd),16)

	def test_username(self):	
		name = os.environ.get('user')
		for c in name:
			if c in string.punctuation:
				self.assertFalse(c)
				break
			else:
				self.assertTrue(c)

	def test_username1(self):	
		uname = os.environ.get('u')
		self.assertGreater(len(uname),6)

	def test_email(self):
	 	temp_mail = os.environ.get('mail')
	 	regexp = re.compile
	 			('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
	 	if regexp.search(temp_mail):
	 		self.assertTrue(temp_mail)
	 	else:
	 		self.assertFalse(temp_mail)
		
	def test_password(self):
	  	temp_pass = os.environ.get('password')
	  	regexp = re.compile('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/')	
	  	if regexp.search(temp_pass):
	  		self.assertTrue(temp_pass)
	  	else:
	  		self.assertFalse(temp_pass)

	def product_type(self):
		list=['web','desktop','android']
		string=os.environ.get('product')
		if string in list:
			self.assertTrue(string)
		else:
			self.assertFalse(string)

	def test_product_name_len(self):
	 	prod_name = os.environ.get('prodnamelen')
	 	self.assertGreater(len(prod_name),50)

 	def test_product_description(self):
 		prod_desc = os.environ.get('prod_desc')
 		self.assertGreater(len(prod_desc),1000)	

	def test_valid_form(self):
	    w = User.objects.create(username=os.environ.get('uname'), email=os.environ.get('uemail'))
	    data = {'username': w.username, 'body': w.email,}
	    form = User_inof_form(data=data)
	    self.assertFalse(form.is_valid())

    def test_login_success(self):
    	self.client = Client()
    	self.username = os.environ.get('uname')
    	self.email = 'test@test.com'
    	self.password = os.environ.get('pass')        
    	self.test_user = User.objects.create_user(self.username, self.email, self.password)
    	login = self.client.login(username=self.username, password=self.password)
    	self.assertEqual(login, True)
    	