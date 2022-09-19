from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password


# Create your views here.

@api_view(['GET', 'POST'])
def reg_user(request):
    if request.method == "POST":
        try:
            data = request.data
            serializer = User_RegistrationSerializer(data=data)
            if not User_Registration.objects.filter(Email=data['Email']).exists():
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status': True,
                        'message': "User Registraion was successfull",
                        'data': serializer.data
                    })

                return Response({
                    'status': False,
                    'message': "Invalid Data",
                    'data': serializer.errors
                })
            else:
                return Response({
                    'status': False,
                    'message': "User already exists"
                })

        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': "Something went Wrong!",
            })

# @api_view(['GET','POST'])
# def user_login(request):
#     email = request.data.get("Email")
#     # password = check_password(request.data.get("Password"))
#
#     if User_Registration.objects.filter(Email=email).exists():
#         user = User_Registration.objects.filter(Email=email)
#         return Response({
#             "status": True,
#             "message": "User got successfull",
#             "data": user
#         })


@api_view(['GET', 'POST'])
def reg_blog(request):
    if request.method == "POST":
        try:
            data = request.data
            serializer = User_BlogSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": True,
                    "message": "You blog was saved successfully",
                    "data": serializer.data
                })
            return Response({
                'status': False,
                'message': "Invalid Data",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': "Something went Wrong!",
            })

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
