from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.
class recipes(models.Model):
	recipes_name = models.CharField(max_length=50)
	content      = models.TextField(max_length=1500)
	imgurl 		 = models.CharField(max_length=100)
	timestamp    = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 	 = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.recipes_name

class post(models.Model):
	name      = models.CharField(max_length=50)
	content   = models.TextField()
	updated   = models.DateTimeField(auto_now_add=False,auto_now=True)
	# timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.name
class testerStatus(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=50)
	timestamp = models.CharField(max_length=40)
	timestamp = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
	def __unicode__(self):
		return str(self.status)

class uatStatus(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=50)
	# timestamp = models.CharField(max_length=40)
	timestamp = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))	
	def __unicode__(self):
		return str(self.status)