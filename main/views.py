from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def reg_user(request):
    try:
        data = request.data
        serializer = User_RegistrationSerializer(data=data)
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
