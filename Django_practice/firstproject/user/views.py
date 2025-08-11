from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from rest_framework import status, viewsets
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

class UserRegisterAPIView(APIView):  
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Cart.objects.create(user=user)
            return Response({'message': 'User registered successfully'})
        return Response(serializer.errors)
    

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user      




"""class UserRegisterAPIView(viewsets.ModelViewSet):
    
    def create(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Cart.objects.create(user=user)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""
"""
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serialaizer = UserSerializer(user)
        return Response(serialaizer.data)
    
    def patch(self , request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self , request):
        user = request.user
        user.delete()
        return Response({"message" : "deleted sucess fully"})
    
"""


