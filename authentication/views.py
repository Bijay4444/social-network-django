from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import authenticate
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

class UserLoginView(generics.CreateAPIView):
    serializer_class = serializers.UserLoginSerializer
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)    
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username = serializer.validated_data.get('username'),
            password = serializer.validated_data.get('password'),
        )
        
        print("User: ", user)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'id': user.pk,
                'username': user.get_username(),
                'token': str(token),
                }
            )
        return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)