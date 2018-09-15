from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from . import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token

class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


