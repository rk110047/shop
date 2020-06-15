from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Address
from .serializer import AddressSerializer
from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication

class ShippingAddressCreateAPIView(generics.CreateAPIView):
    queryset                        =   Address.objects.all()
    serializer_class                =   AddressSerializer
    permission_classes              =   []
    authentication_classes          =   [SessionAuthentication]


    def post(self,request,*args,**kwargs):
        self.create(request,*args,**kwargs)
        return Response({"message":"posted"}) 

    def perform_create(self,serializer):
        billingprofile       =   self.request.user.billingprofile
        serializer.save(billingprofile=billingprofile)

class BillingAddressCreateAPIView(generics.CreateAPIView):
    queryset                        =   Address.objects.all()
    serializer_class                =   AddressSerializer
    permission_classes              =   []
    authentication_classes          =   [SessionAuthentication]


    def post(self,request,*args,**kwargs):
        self.create(request,*args,**kwargs)
        return Response({"message":"posted"})

    def perform_create(self,serializer):
        billingprofile       =   self.request.user.billingprofile
        serializer.save(billingprofile=billingprofile,address_type="BILLING")
