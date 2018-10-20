from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from serializers import  userBalanceSerializer,UserSerializer, UserMobileNumber,isApprovedSerial
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from models import userBalance, userInfo, isApproved
from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.decorators import api_view
from django.db.models import Q


from rest_framework.authtoken.models import Token


class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = user
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class updateUserBalance(generics.RetrieveUpdateDestroyAPIView):
    lookup_fields = 'pk'
    serializer_class =  userBalanceSerializer
    def get_queryset(self):
        return userBalance.objects.all()
    def get_object(self):
        pk = self.kwargs.get("pk")
        return userBalance.objects.get(pk=pk)

class userMobileNumber(generics.ListAPIView):
    # def get(self, request):
    #     username =  self.kwargs['username']
    #     print username
    #     user = User.objects.get(username=userName)
    #     mobileNumber = userInfo.filter(user__username = username)
    #     serializer = UserMobileNumber(mobileNumber, many=True)
    #     return Response(serializer.data)
    serializer_class = UserMobileNumber
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = userInfo.objects.all()
        username =  self.kwargs['username']
        print username      
        queryset = queryset.filter(user__username = username)
        return queryset
    # def post(self, request):

class isApprovedView(generics.ListAPIView):
    serializer_class = isApprovedSerial
    def get_queryset(self):
        queryset = isApproved.objects.all()
        username =  self.kwargs['username']
        queryset = queryset.filter(user__username = username)
        return queryset

class CreateMobileNumberView(CreateAPIView):
    queryset = userInfo.objects.all()
    serializer_class = UserMobileNumber

class getUserBalance(generics.ListAPIView):
    serializer_class = userBalanceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = userBalance.objects.all()
        username =  self.kwargs['username']
        print username      
        queryset = queryset.filter(user__username = username)
        return queryset



