from rest_framework import serializers
from profiles_api import models # this will allow us to access our user model

class HelloSerializer(serializers.Serializer):
    """serializes our name field for testing our APIVIew"""
    name = serializers.CharField(max_length=10)


#creating a model serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    #we always use meta calss to assign the fields which we want to serializer
    class Meta:
        model = models.UserProfile
        # list of fields which you want to make accessible
        fields = ('id', 'email', 'name', 'password')
        #we don't want to allow the user to retreve the password
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

        #overriding the default function provided by the ModelSerializer Class
    def create(self, validated_data):
        """ Creates and returns a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handels updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
