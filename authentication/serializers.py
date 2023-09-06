from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
            model = models.CustomUser
            fields = ['id', 'email','username', 'password', 'confirm_password']
        
    def validate(self, attrs):
            if attrs.get('password')!=attrs.get('confirm_password'):
                raise serializers.ValidationError("Password and Confirm Password does not match")
        
            return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')  # Remove confirm_password from validated_data

        user = models.CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'user', 'bio', 'profile_image', 'follows', 'followed_by', 'updated', 'created')
        

class UserLoginSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(read_only=True)
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(write_only=True)
    token=serializers.CharField(read_only=True)
    class Meta:
        model=models.CustomUser
        fields=['id','username','password','token']