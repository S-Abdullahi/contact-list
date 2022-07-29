import email
from turtle import write_docstringdict
from dataclasses import field, fields
from xmlrpc.client import ResponseError
from django.contrib.auth.models import User
from django.forms import PasswordInput
from rest_framework import serializers
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
                                      
    class Meta:
        model = User
        fields  = ('id', 'username' ,'email', 'password')
        extra_kwargs = {
            'password' : {'write_only': True}
        }
        
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']   
        user = User.objects.create_user(username, email, password)
        return user
        
    # def save(self):
        
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']
    #     # email = self.validated_data['email']
    #     username = self.validated_data['username']
        
    #     if password != password2:
    #         raise serializers.ValidationError({'error': 'Password one and password two not the same.'})
        
    #     # if User.objects.filter(email).exists():
    #     #     raise serializers.ValidationError({'error': 'Email already exists.'})
        
    #     reg = User(username) 
    #     reg.set_password(password)
    #     reg.save()
        
    #     return reg