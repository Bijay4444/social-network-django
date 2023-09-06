from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

class UserLoginView(generics.CreateAPIView):
    serializer_class = serializers.UserLoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)   
        serializer.is_valid(raise_exception=True)
    
        user = authenticate(username=serializer.validated_data.get('username'), 
                            password=serializer.validated_data.get('password'),
                            )
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'id': user.pk,
                'username': user.get_username(),
                'token':str(token),
                             
             }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)