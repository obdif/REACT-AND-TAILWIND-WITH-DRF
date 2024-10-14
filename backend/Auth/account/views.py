from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny



class RegisterUserView(generics.CreateAPIView):
    serializer_class=UserRegisterSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=  serializer.data
            
            
            return Response({
                'data':user,
                'message': f"hi {user['email']} thanks for signing up"
            }, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginUser(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        
        if serializer.is_valid(raise_exception=True):
            return Response({
                'message':"you have successfully login"
            })
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        

class DeleteUser(GenericAPIView):
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)