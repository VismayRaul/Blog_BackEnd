from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer

# Create your views here.


# class UserList(generics.ListCreateAPIView):
#     serializer_class = User_RegistrationSerializer
#
#     def get_queryset(self):
#         queryset = User_Registration.objects.all()
#         users = self.request.query_params.get('email')
#         if users is not None:
#             queryset = queryset.filter(email=users)
#         return queryset
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = User_RegistrationSerializer
#     queryset = User_Registration.objects.all()





