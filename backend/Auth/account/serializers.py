from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed





class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model= User
        fields = [
            'email', 'password', 'password2'
        ]
    
    def validate(self, attrs):
        
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        
        if password != password2:
            raise serializers.ValidationError('passsword do not match')
        return attrs
        # return super().validate(attrs)
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data.get('password')
        )
        
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=5)
    password = serializers.CharField(max_length=50, write_only=True)
    
    
    class Meta: 
        model= User
        fields = [
            'email', 'password'
        ]
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed('invalid Credentials, Try again')
        
        return{
            'email': user.email
        }