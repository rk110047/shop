from django.shortcuts import render
from .models import CustomerProfile
from rest_framework.authentication import SessionAuthentication
from .serializer import CustomerProfileSerializer
from rest_framework import  generics



class CreateProfileAPIView(generics.CreateAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication]

    def perform_create(self,serializer):
        serializer.save(User=self.request.user,email=self.request.user.email)




class EditProfileAPIView(generics.UpdateAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       []
    lookup_field            =       'username'


class CustomerListAPIView(generics.ListAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       []
