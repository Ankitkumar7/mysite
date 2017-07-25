# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Day one modal
class dayOne(models.Model):
	title = models.CharField(max_length=50)
	setone = models.CharField(max_length=500)
	settwo = models.CharField(max_length=500, null=True)
	exercisetime = models.FloatField()
	imagelink = models.CharField(max_length=500)

	def __str__(self):
		return self.title
# Day two modal
class dayTwo(models.Model):
	title = models.CharField(max_length=50)
	setone = models.CharField(max_length=500)
	settwo = models.CharField(max_length=500, null=True)
	exercisetime = models.FloatField()
	imagelink = models.CharField(max_length=500)

	def __str__(self):
		return self.title

class dayThree(models.Model):
	title = models.CharField(max_length=50)
	setone = models.CharField(max_length=500)
	settwo = models.CharField(max_length=500, null=True)
	setthree = models.CharField(max_length=500, null=True)
	exercisetime = models.FloatField()
	imagelink = models.CharField(max_length=500)

	def __str__(self):
		return self.title
class dayFour(models.Model):
	title = models.CharField(max_length=50)
	setone = models.CharField(max_length=500)
	settwo = models.CharField(max_length=500, null=True)
	settthree = models.CharField(max_length=500, null=True)
	exercisetime = models.FloatField()
	imagelink = models.CharField(max_length=500)

	def __str__(self):
		return self.title
class dayFive(models.Model):
	title = models.CharField(max_length=50)
	setone = models.CharField(max_length=500)
	settwo = models.CharField(max_length=500, null=True)
	settthree = models.CharField(max_length=500, null=True)
	exercisetime = models.FloatField()
	imagelink = models.CharField(max_length=500)

	def __str__(self):
		return self.title

class daySix(models.Model):
	title = models.CharField(max_length=50)
	setone = models.CharField(max_length=500)
	settwo = models.CharField(max_length=500, null=True)
	settthree = models.CharField(max_length=500, null=True)
	exercisetime = models.FloatField()
	imagelink = models.CharField(max_length=500)

	def __str__(self):
		return self.title


class music(models.Model):
    title =  models.CharField(max_length=200)
    url = models.CharField(max_length=2000)
    def __str__(self):
		return self.title

class userAddDiet(models.Model):
	dietName = models.CharField(max_length=200)