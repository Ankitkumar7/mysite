# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import dayOne, dayTwo, dayThree, dayFour, dayFive, daySix, music
from .serializers import StockSerializerOne, StockSerializerTwo, StockSerializerThree, StockSerializerFour, StockSerializerFive, StockSerializerSix,StockSerializerMusic

from .models import dayOne, dayTwo, dayThree, dayFour, dayFive, daySix, music





# Get the data from day one model
class dayOneView(APIView):
	def get(self, request):
		dayone = dayOne.objects.all()
		serializer = StockSerializerOne(dayone, many=True)
		return Response(serializer.data)
	def post(self, request):
		pass
# Get the data from day two model
class dayTwoView(APIView):
	def get(self, request):
		dayone = dayTwo.objects.all()
		serializer = StockSerializerTwo(dayone, many=True)
		return Response(serializer.data)
	def post(self, request):
		pass
class dayThreeView(APIView):
	def get(self, request):
		dayone = dayThree.objects.all()
		serializer = StockSerializerThree(dayone, many=True)
		return Response(serializer.data)
	def post(self, request):
		pass

class dayFourView(APIView):
	def get(self, request):
		dayone = dayFour.objects.all()
		serializer = StockSerializerFour(dayone, many=True)
		return Response(serializer.data)
	def post(self, request):
		pass
class dayFiveView(APIView):
	def get(self, request):
		dayone = dayFive.objects.all()
		serializer = StockSerializerFive(dayone, many=True)
		return Response(serializer.data)
	def post(self, request):
		pass
class daySixView(APIView):
	def get(self, request):
		dayone = daySix.objects.all()
		serializer = StockSerializerSix(dayone, many=True)
		return Response(serializer.data)
	def post(self, request):
		pass

class music_view(APIView):
	def get(self, request):
		dayone = music.objects.all()
		serializer = StockSerializerMusic(dayone, many=True)
		return Response(serializer.data)


