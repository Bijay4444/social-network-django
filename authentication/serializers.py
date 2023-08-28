from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'date_of_birth')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = models.CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'user', 'bio', 'profile_image', 'follows', 'followed_by', 'updated', 'created')
        
    