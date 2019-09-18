from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing """

    name = serializers.CharField(max_length=20)


class  UserProfileSerializer(serializers.ModelSerializer):
    """ Serializer for profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #add in extra attributes added for any of the fields
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return new user """
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
