from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)