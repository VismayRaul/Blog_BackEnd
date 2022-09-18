from rest_framework import serializers
from .models import User_Registration, User_Blog

class User_RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Registration
        fields = "__all__"

class User_BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Blog
        fields = "__all__"