from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from models import userBalance, userInfo, isApproved

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class userBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = userBalance
        fields = [
            'pk',
            'balance',
            'user'
        ]

class UserMobileNumber(serializers.ModelSerializer):
    class Meta:
        model = userInfo
        fields = [
            'user',
            'mobileNumber'
        ]

class isApprovedSerial(serializers.ModelSerializer):
    class Meta:
        model = isApproved
        fields = [
            'user',
            'isApproved'
        ]