from rest_framework import serializers
from .models import User_Registration, User_Blog
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

class User_RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Registration
        fields = "__all__"


    def createuser(self, validated_data):
        user = User_Registration.objects.create(
            FirstName=validated_data['FirstName'],
            LastName=validated_data['LastName'],
            Email=validated_data['Email'],
            Password=make_password(validated_data['Password'])
        )
        user.save()
        return user

class User_BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Blog
        fields = "__all__"

        def createblog(self, validated_data):
            blog = User_Blog.objects.create(
                Title=validated_data['Title'],
                Content=validated_data['Content'],
                Description=validated_data['Description'],
                Author=validated_data['Author']
            )
            blog.save()
            return blog