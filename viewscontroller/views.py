from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from serializers import  userBalanceSerializer,UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from models import userBalance
from rest_framework.decorators import api_view

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
                json['token'] = token.key
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

