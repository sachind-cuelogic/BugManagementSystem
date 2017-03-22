from django.test import TestCase
from forms import User_inof_form
from django import forms
import re
from django.contrib.auth.models import User
import string
import unittest



class FormTestCase(TestCase):
	def test_form(self):
		self.assertTrue(User.objects.create_user(username="sacc", email="sacc@mail.com",password="abcde123"))

	def test_email(self):
		temp_mail = 'sachin@mail.com'
		regexp = re.compile('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
		if regexp.search(temp_mail):
			self.assertTrue(temp_mail)
		else:
			self.assertFalse(temp_mail)

	def test_username(self):	
		name = "sachin"
		for c in name:
			if c in string.punctuation:
				self.assertFalse(c)
				
			else:
				self.assertTrue(c)
				
	def test_pass1_pass2(self):
		pass1 = "sachin"
		pass2 = "sachinasdf"
		#self.assertEqual(pass1,pass2)
		self.assertNotEqual(pass1, pass2)

